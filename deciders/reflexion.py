import openai
from .misc import history_to_str
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain import LLMChain
from loguru import logger
from langchain.callbacks import FileCallbackHandler
from langchain_community.callbacks import get_openai_callback
from .act import NaiveAct
from memory.env_history import EnvironmentHistory
import tiktoken
from .utils import get_chat, num_tokens_from_string


class Reflexion(NaiveAct):
    def __init__(self, action_space, args, prompts, distiller, temperature=0.1, max_tokens=None, logger=None):
        super().__init__(action_space, args, prompts, distiller, temperature, max_tokens, logger)

    def act(
        self,
        state_description,
        action_description,
        env_info,
        game_description,
        goal_description,
        logfile=None,
    ):
        self.action_description = action_description
        self.game_description = game_description 
        self.goal_description = goal_description
        # self.env_history.add("observation", state_description)
        self._add_history_before_action(game_description, goal_description, state_description)
        messages = []
        messages.append({"role": "system", "content": f"You are a superior game player. Now, you are completing a challenging task. You must carefully understand the Reflexion method you will use and apply it to the following task. You are in a game. {game_description}\n {goal_description} "})
        
        # task-irrelevant SystemMessage
        # if self.irr_few_shot_examples:
        #     for i, examples in enumerate(self.irr_few_shot_examples):
        #         messages.append({"role": "system", "name": "example_user", "content": examples['question']})
        #         messages.append({"role": "system", "name": "example_assistant", "content": examples['answer']})

        # if self.fewshot_example:
        #     for i, examples in enumerate(self.fewshot_example):
        #         messages.append({"role": "system", "name": "example_user", "content": examples['question']})
        #         messages.append({"role": "system", "name": "example_assistant", "content": examples['answer']})


        if self.prompt_level in [2, 3, 4]:
            if self.memory:
                if self.prompt_level == 2:
                    role_name = "example_user with random policy"
                elif self.prompt_level == 3:
                    role_name = "example_user"
                elif self.prompt_level == 4:
                    role_name = "example_user with expert policy"
                for mem in self._read_mem():
                    messages.append({"role": "system", "name": role_name,  "content": mem})

        if self.use_short_mem:
            if len(self.env_history) > 1:
                messages.append({"role": "user",  "content":  f"Your historical experiences are: {self.env_history.get_histories(self.mem_num)}"})

        instruction =  f'Currently, {state_description} {action_description}\n You should first take a deep breath. Then you should think step by step about the action selection and  lay out your thought process explicitly. After that you should decide an action based on the thought. For the whole response, you should use JSON format with two keys "Thought Process" and "action". '
        instruction_msg = {"role": "user", "content": instruction}
        for i in range(len(messages)):
            if num_tokens_from_string(self.args.gpt_version, messages[:i]) > self.args.max_query_tokens-num_tokens_from_string(self.args.gpt_version, instruction_msg):
                messages = messages[:i-1]
                break
        messages.append(instruction_msg)
        response, usage = get_chat(self.client, messages, api_type=self.args.api_type, model=self.args.gpt_version, temperature=self.temperature, max_tokens=self.max_generate_tokens, seed=self.seed)
        action_str = response
        print(f'my anwser is {action_str}')
        for _ in range(5):
            try:
                action = self.reg_parse(response)
                if action is None:
                    action = self.parser.parse(response).action
                break
            except:
                continue
        if not self.logger:
            logger.remove()
            self.logger = logger.add(logfile, colorize=True, enqueue=True)
        self._add_history_after_action(action)
        self.logger.info(f'The GPT prompt is: {messages}.')
        self.logger.info(f'The GPT response is: {response}.')
        self.logger.info(f'The optimal action is: {action}.')
        if env_info.get('history'):
            self.logger.info(f'History: {history_to_str(env_info["history"])}')
        token, cost = usage["token"], usage["cost"]
        self.logger.info(f'Token Usage: {token}; Cost Usage: {cost} $.')
        self.cum_token_usage += token
        self.cum_cost_usage += cost
        self.logger.info(f'Cummulative Token Usage: {self.cum_token_usage}; Cummulative Cost Usage: {self.cum_cost_usage} $.')

        return action, messages, response, token, cost
