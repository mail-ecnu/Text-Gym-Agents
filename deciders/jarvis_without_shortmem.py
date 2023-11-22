import openai
from .misc import history_to_str
from langchain.chat_models import AzureChatOpenAI
from langchain.prompts.chat import (
    PromptTemplate,
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain import LLMChain
from loguru import logger
from langchain.callbacks import FileCallbackHandler
from langchain.callbacks import get_openai_callback
from .act import NaiveAct
from memory.env_history import EnvironmentHistory
import tiktoken
from .utils import run_chain


class JarvisWithoutShortMem(NaiveAct):
    def __init__(self, action_space, args, prompts, distiller, temperature=0.1, max_tokens=None):
        super().__init__(action_space, args, prompts, distiller, temperature, max_tokens)
        self.pre_memory = []
        self.post_memory = []
        self.is_first = True
        self.num_trails = args.num_trails
        self.game_description = args.game_description
        self.goal_description = args.goal_description
        self.action_description = args.action_description
        self._update_mem(None)
    
    def update_mem(self,):
        traj = self.game_description 
        traj += self.goal_description
        max_step_num = min(14000 // self.num_tokens_from_string(self.env_history.get_one_history()),200)
        traj += self.env_history.get_histories(max_step_num)
        self._update_mem(traj)

    def _update_mem(self, traj):
        if not self.is_first:
            summary = self.distiller.generate_summary(traj, self.post_memory)
            self.post_memory.append(summary)
            self.insight = self.distiller.generate_insight(self.post_memory)
        else:
            self.is_first = False
        suggestion = self.distiller.generate_suggestion(self.game_description, self.goal_description, self.action_description, self.pre_memory, self.post_memory, self.num_trails)
        self.pre_memory.append(suggestion)
        self.env_history.reset()

    def _read_mem(self, ):
        insight_str = ""
        if len(self.post_memory) > 0:
            insight_str += "The insights of the game are listed below: "
            insight_str += f"{self.insight}\n"
        suggestion_str = "The suggestions are listed below:" + self.pre_memory[-1]
        return insight_str + suggestion_str 

    def act(
        self,
        state_description,
        action_description,
        env_info,
        game_description,
        goal_description,
        logfile=None,
    ):
        self.game_description = game_description 
        self.goal_description = goal_description
        self.env_history.add("observation", state_description)
        chat = AzureChatOpenAI(
            openai_api_type=openai.api_type,
            openai_api_version=openai.api_version,
            openai_api_base=openai.api_base,
            openai_api_key=openai.api_key,
            deployment_name=self.args.gpt_version,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        reply_format_description = \
            "Your response should choose an optimal action from valid action list, and terminated with following format: "        
            # only task relevant examplesA
        template = "Now you are completing a task. "
        template += "You need to carefully understand the description of the game. " 
        # TODO: few shot example handle
        if self.irr_few_shot_examples:
            template += "Here are some examples of how you should completing a task."
            for examples in self.irr_few_shot_examples:
                template += "\nQuestion: \n" + examples['question'] + "Answer: \n" + examples['answer']
        
        if self.fewshot_example:
            if self.expert_knowledge:
                template += "Here, I will provide you with some expert knowledge to help you better understand the rules of the task."
                template += self.expert_knowledge + '\n'
            template += "Next are some examples: "
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)

        human_template = ""
        human_template += "\n\nNow you are in the task.\n" 
        human_template += "{game_description}\n{action_description}\n{goal_description}\n"
        human_template += "You are observing something and  " \
                "you need to choose the optimal action acoordingly. "
        human_template += 'Response and interact using the format: {reply_format_description}{format_instructions}\n'
        human_template += self._read_mem()
        human_template += "\n\nHere are some history states listed below:\n"
        
        fewshot_example_prompt = PromptTemplate(
            input_variables=["question", "answer"],
            template="Question: \n{question}\n{answer}"
        )
        human_message_prompt = FewShotPromptTemplate(
            examples=self.fewshot_example,
            example_prompt=fewshot_example_prompt,
            suffix=human_template,
            input_variables=[
                'game_description', 'goal_description',
                'action_description', 'reply_format_description'],
            partial_variables={'format_instructions': self.parser.get_format_instructions()}
        )
        human_message_prompt = HumanMessagePromptTemplate(prompt=human_message_prompt)

        short_memory_template = HumanMessagePromptTemplate.from_template("{history} Please select an action based on the current game state:")

        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt, short_memory_template])

        
        if logfile:
            # logger.remove()
            if self.first_call:
                logger.add(logfile, colorize=True, enqueue=True, filter=lambda x: '[Reflexion Memory]' not in x['message'])
                self.first_call = False
            handler = FileCallbackHandler(logfile)
        total_tokens, total_cost = 0, 0 
        max_think_times = 1
        # TODO: ADD REACT Support
        # print(str(self.env_history))
        if self.use_short_mem: 
            my_history = str(self.env_history)
        else:
            my_history = ""
        for i_think in range(max_think_times):
            chain = LLMChain(llm=chat, prompt=chat_prompt, callbacks=[handler], verbose=False)
            with get_openai_callback() as cb:
                response = run_chain(
                    chain,
                    game_description=game_description,
                    goal_description=goal_description,
                    action_description=action_description,
                    history=self.env_history.get_last_history(),
                    format_instructions=self.parser.get_format_instructions(),
                    reply_format_description=reply_format_description,
                    max_token = 3000
                )

                total_tokens += cb.total_tokens
                total_cost += cb.total_cost
            action = self.parser.parse(response).action

        text_prompt = chat_prompt.format_messages(
            game_description=game_description,
            goal_description=goal_description,
            action_description=action_description,
            history=self.env_history.get_last_history(),
            format_instructions=self.parser.get_format_instructions(),
            reply_format_description=reply_format_description,
        )
        texts = ""
        for text in text_prompt:
            texts += text.content + "\n"

        self._add_history_after_action(action)
        logger.info(f'The GPT response is: {response}.')
        logger.info(f'The optimal action is: {action}.')
        if self.pre_memory:
            logger.info(f'The suggestion is: {self.pre_memory[-1]}.')
        if self.post_memory:
            logger.info(f'The summary is: {self.post_memory[-1]}.')
        if env_info.get('history'):
            logger.info(f'History: {history_to_str(env_info["history"])}')

        return action, texts, response, logger, total_tokens, total_cost
