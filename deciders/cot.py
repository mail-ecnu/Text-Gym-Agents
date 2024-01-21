import openai
from .misc import history_to_str
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from loguru import logger
from .act import NaiveAct
from .utils import run_chain, get_chat  


class ChainOfThought(NaiveAct):
    def __init__(self, action_space, args, prompts, distiller, temperature=0.1, max_tokens=None, logger=None):
        super().__init__(action_space, args, prompts, distiller, temperature, max_tokens,logger)

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
        self._add_history_before_action(game_description, goal_description, state_description)
        messages = []
        messages.append({"role": "system", "content": f"You are a helpful assistant. You must carefully understand the Chain-of-Thought method you will use and apply it to the following task. You are in a game. {game_description}\n {goal_description} " })
        
        # task-irrelevant SystemMessage
        if self.irr_few_shot_examples:
            for i, examples in enumerate(self.irr_few_shot_examples):
                messages.append({"role": "system", "name": "example_user", "content": examples['question']})
                messages.append({"role": "system", "name": "example_assistant", "content": examples['answer']})

        if self.fewshot_example:
            for i, examples in enumerate(self.fewshot_example):
                messages.append({"role": "system", "name": "example_user", "content": examples['question']})
                messages.append({"role": "system", "name": "example_assistant", "content": examples['answer']})

        if self.prompt_level in [2, 3, 4]:
            if self.memory:
                if self.prompt_level == 2:
                    role_name = "example_user_with_random_policy"
                elif self.prompt_level == 3:
                    role_name = "example_user"
                elif self.prompt_level == 4:
                    role_name = "example_user_with_expert_policy"
                for mem in self._read_mem():
                    messages.append({"role": "system", "name": role_name,  "content": mem})

        if self.use_short_mem:
            if len(self.env_history) > 1:
                messages.append({"role": "user",  "content":  f"{self.env_history.get_histories(self.mem_num)}"})


        instruction = f"{state_description}.{action_description}\n Please suggest an action based on the current game state and the information you get. You must select the appropriate action from the given action descriptions and cannot refrain from taking action or performing any prohibited actions. Please note that you need to carefully lay out your thought process on the question, not just give an answer. You need to write the corresponding logic of your thinking following the example above. Make sure you give an valid action! Your Suggested Action is: "
        instruction_msg = {"role": "user", "content": instruction}
        for i in range(len(messages)):
            if num_tokens_from_string(self.args.model, messages[:i]) > self.args.max_query_tokens-num_tokens_from_string(self.args.model, instruction_msg):
                messages = messages[:i-1]
                break
        messages.append(instruction_msg)

        response, usage = get_chat(messages, api_type=self.args.api_type, model=self.args.gpt_version, temperature=self.temperature, max_tokens=self.max_generate_tokens, seed=self.seed)
        action_str = response
        print(f'my anwser is {action_str}')
        action = self.parser.parse(response).action
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
