# This file contains functions for interacting with the ChatGPT model

import openai
from .gpt import gpt 
from loguru import logger
from .parser import DISPARSERS, CONPARSERS
from langchain.output_parsers import PydanticOutputParser
from langchain.output_parsers import OutputFixingParser
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from memory.env_history import EnvironmentHistory
import tiktoken
import json
import re
from .utils import run_chain, get_chat
from gym.spaces import Discrete

class RandomAct():
    def __init__(self, action_space):
        self.action_space = action_space
    
    def act(self, state_description, action_description, env_info, game_description=None, goal_description=None):
        if isinstance(self.action_space, Discrete):
            action = self.action_space.sample()+1
        else:
            action = self.action_space.sample()
        return action, '', '', '', 0, 0

class NaiveAct(gpt):
    def __init__(self, action_space, args, prompts, distiller, temperature=0.0, max_tokens=2048, logger=None):
        self.action_space = action_space
        self.temperature = temperature
        self.action_desc_dict = args.action_desc_dict
        self.args = args
        self.seed = args.seed 
        self.prompts = prompts
        self.max_tokens = max_tokens
        self.cum_token_usage = 0
        self.cum_cost_usage = 0
        self.prompt_level = args.prompt_level
        if args.gpt_version == "gpt-35-turbo":
            model = "gpt-3.5-turbo"
        else:
            model = args.gpt_version
        self.encoding = tiktoken.encoding_for_model(model)
        super().__init__(args)
        self.distiller = distiller
        self.fewshot_example_initialization(args.prompt_level, args.prompt_path, distiller = self.distiller)
        if isinstance(self.action_space, Discrete):
            self.default_action = 1
        else:
            self.default_action = [0 for ind in range(self.action_space.shape[0])]
        self.parser = self._parser_initialization()
        self.irr_game_description = ''
        self.memory = []
        self.env_history = EnvironmentHistory()
        self.first_call = True
        self.logger = logger
        if self.prompt_level in [2, 4]: 
            self.memory = self.summarized_fewshot_example
        if args.use_short_mem == 1: 
            self.use_short_mem = True
            self.mem_num = self.args.short_mem_num
        else:
            self.use_short_mem = False
            self.mem_num = 0
        

    def num_tokens_from_string(self,string: str) -> int:
        """Returns the number of tokens in a text string."""
        num_tokens = len(self.encoding.encode(string))
        return num_tokens

    def update_mem(self,):
        traj = "Firstly, the description and the goal of the task will be provided. Please pay close attention to comprehend the information presented below.\n"
        traj += "Task Description: " + self.game_description + '\n'
        traj += "Goal Description: " + self.goal_description + '\n'
        traj += self.action_description
        traj += "Below is the historical data for this round of the game, which includes the state and corresponding action for each step.\n"
        traj += str(self.env_history)
        # print(traj)
        self._update_mem(traj)

    def _update_mem(self, traj):
        my_reflection = self.distiller.generate(traj, self.memory)
        self.memory.append(my_reflection)
        self.env_history.reset()

    def clear_mem(self):
        self.update_mem()
        self.pre_memory = []
        self.post_memory = []
        self.is_first = True
        self.env_history.reset()


    def _parser_initialization(self):
        if isinstance(self.action_space, Discrete): 
            PARSERS = DISPARSERS
            num_action = self.action_space.n
        else: 
            PARSERS = CONPARSERS
            num_action = self.action_space.shape[0]

        if self.args.api_type == "azure":
            autofixing_chat = AzureChatOpenAI(
                openai_api_type=openai.api_type,
                openai_api_version=openai.api_version,
                azure_endpoint=openai.azure_endpoint,
                openai_api_key=openai.api_key,
                model=self.args.gpt_version,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                seed=self.seed
            )
        elif self.args.api_type == "openai":
            autofixing_chat = ChatOpenAI(temperature=self.temperature, openai_api_key=openai.api_key,model=self.args.gpt_version, seed=self.seed)

        parser = PydanticOutputParser(pydantic_object=PARSERS[num_action])
        autofixing_parser = OutputFixingParser.from_llm(
            llm=autofixing_chat, parser=parser)
        return autofixing_parser

    def fewshot_example_initialization(self, level, path=None, distiller=None):
        self.fewshot_example = []
        self.irr_few_shot_examples = []
        self.prompt_level = level
        self.expert_knowledge = None
        if level in [1,3]:
            self.irr_few_shot_examples = self.prompts.TASK_IRRELEVANT_PROMPTS
        elif level == 5:
            if hasattr(self.prompts, "expert_prompt"):
                self.expert_knowledge = self.prompts.expert_prompt
            self.fewshot_example = self.prompts.PERCEPTRON_BASIC_FS_EXAMPLES
        else:
            self.irr_few_shot_examples = self.prompts.TASK_IRRELEVANT_PROMPTS
            json_file = f'{path}_l{level}.json'
            with open(json_file, 'r') as infile:
                data = json.load(infile)
            max_step_num = 0
            for traj in data: 
                traj_text = traj[0]['game_description']
                traj_text += traj[0]['goal_description']
                for i, transition in enumerate(traj): 
                    traj_text += transition['observation']
                    traj_text += f"> {transition['action']}"
                    traj_text += f"{transition.get('reward','')}\n"
                    one_traj_token = self.num_tokens_from_string(traj_text)
                    if one_traj_token > self.args.max_query_tokens:
                        max_step_num = i+1
                        break
                traj_text += f"Your performance is: {transition['cum_reward']}"
            if not max_step_num:
                max_step_num = self.args.max_episode_len
            self.summarized_fewshot_example = self.distiller.generate_from_file(json_file,max_step_num=max_step_num)

    def response(self, state_description, action_description, env_info, game_description=None, goal_description=None, fewshot_examples=None):
        instruction = "Please select an action based on the current game state and the information you get. You must select the appropriate action from the given action descriptions and cannot refrain from taking action or performing any prohibited actions. Your Action is: "
        messages = []
        messages.append({"role": "system", "content": f"You are a helpful assistant. You are in a game. {game_description}\n {goal_description}"})
        for my_msg in fewshot_examples:
            messages.append(my_msg)
        messages.append({"role": "user", "content": f"{state_description}.{action_description}\n{instruction}"})
    
        res, usage = get_chat(messages, api_type=self.args.api_type, model=self.args.gpt_version, temperature=self.temperature, max_tokens=self.max_tokens, seed=self.seed)
        return messages, res, usage
    
    def _add_history_before_action(self, game_description, goal_description, state_description):
        self.game_description = game_description 
        self.goal_description = goal_description
        self.env_history.add("observation", state_description)

        # limit the token used, or it may exceed the max token
        if len(self.env_history):
            one_history_token = self.num_tokens_from_string(self.env_history.get_one_history())
            self.env_history.set_history(self.args.max_query_tokens // one_history_token)

    def act(self, state_description, action_description, env_info, game_description=None, goal_description=None, logfile=None):
        self.action_description = action_description
        self._add_history_before_action(game_description, goal_description, state_description)
        asking_round = 0
        res = None
        action = None
        if not self.logger:
            logger.remove()
            self.logger = logger.add(logfile, colorize=True, enqueue=True)
        
        example_messages = []
        if self.args.prompt_level == 5:    
            if self.fewshot_example:
                for examples in self.fewshot_example:
                    example_messages.append({"role": "system", "name":"example_user",  "content": examples['question']})
                    example_messages.append({"role": "system", "name":"example_assistant",  "content": examples['answer']})
        elif self.args.prompt_level in [2,3,4]:
            if self.prompt_level == 2:
                role_name = "example_user with random policy"
            elif self.prompt_level == 3:
                role_name = "example_user"
            elif self.prompt_level == 4:
                role_name = "example_user with expert policy"
            for mem in self._read_mem():
                example_messages.append({"role": "system", "name": role_name,  "content": mem})
        
        if self.use_short_mem:
            if len(self.env_history) > 1:
                example_messages.append({"role": "user",  "content":  f"{self.env_history.get_histories(self.mem_num)}"})
        
        messages, response, usage = self.response(state_description, action_description, env_info, game_description, goal_description, example_messages)
        
        action_str = response
        print(f'my anwser is {action_str}')
        action = self.parser.parse(response).action
        self._add_history_after_action(action)
        self.logger.info(f'The GPT response is: {response}.')
        self.logger.info(f'The action is: {action}.')
        if env_info.get('history'):
            self.logger.info(f'History: {history_to_str(env_info["history"])}')
        token, cost = usage["token"], usage["cost"]
        self.logger.info(f'Token Usage: {token}; Cost Usage: {cost} $.')
        self.cum_token_usage += token
        self.cum_cost_usage += cost
        self.logger.info(f'Cummulative Token Usage: {self.cum_token_usage}; Cummulative Cost Usage: {self.cum_cost_usage} $.')
        return action, messages, response, self.cum_token_usage, self.cum_cost_usage

    def _read_mem(self, ):
        memory = self.memory
        mem_lst = []
        if len(memory) > 5:
            memory = memory[-5:]
        if len(memory) > 0:
            for i, m in enumerate(memory):
                mem_lst.append(f'\nTrial {i}:\n{m.strip()}')
        return mem_lst
        
    def _add_history_after_action(self, action):
        self.env_history.add('action', action)