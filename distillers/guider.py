from deciders.utils import get_completion, get_chat

from typing import List, Dict, Any
from loguru import logger
import random 
import json
class Guidance_Generator():
    def __init__(self,logfile="",args=None):
        self.args = args
        with open("./distillers/guidance_summary_few_shot_examples.txt", 'r') as f:
            self.SUMMARY_FEW_SHOT_EXAMPLES = f.read()
        self.insight = ""
        self.suggestion = ""
        if logfile:
            # logger.remove()
            logger.add(logfile, colorize=True, enqueue=True, filter=lambda x: '[Reflexion Memory]' in x['message'])
    
    def generate_from_file(self, file_path,max_step_num=200):
        mem = []
        with open(file_path, 'r') as infile:
            data = json.load(infile)
        for traj in data: 
            traj_text = traj[0]['game_description']+'\n'
            traj_text += traj[0]['goal_description']+'\n'
            for transition in traj[-max_step_num:]: 
                traj_text += transition['observation']+'\n'
                if type(eval(str(transition['action']))) == type([]):
                    action = float(eval(str(transition['action']))[0])-1
                else:
                    action = transition['action']
                traj_text += f"Action: {action}\n"
                traj_text += f"Reward: {transition['reward']}\n"
            traj_text += f"Your performance is: {transition['cum_reward']}\n"
            summary = self.generate_summary(traj_text, mem)
            mem.append(summary)
        return mem

    def _generate_summary_query(self, traj, post_memory):
        """
        Generates an exploration guidance query for GPT-3.5 based on given trajectory and memory.
        
        Parameters:
        - traj: Trajectory of the new experience.
        - post_memory: List of memory items to summarize.

        Returns:
        - query: Formulated query string for GPT-3.5.
        """
        segments = []

        # Trajectory
        segments.append(f"Your new collected trajectory is as below:\n {traj}")
        segments.append(f"The suggestion to guide the trajectory is:\n{self.suggestion}")
        # Questions
        questions = """
        Please answer the following questions directly, without additional explanation:
        1. Based on the collected trajectory, infer the specific values of game-relevant knowledge proposed in the suggestion with json format.
        2. Summarize the policy behavior and its performance.
        Provide concise responses.
        """
        segments.append(questions)

        # Construct the final query
        query = '\n'.join(segments)
        return query


    def generate_summary(self, traj, post_memory):
        query = self._generate_summary_query(traj, post_memory)
        summary = get_chat(query,model=self.args.gpt_version, engine=self.args.gpt_version)
        logger.info(f'[Reflexion Memory]The summary prompt is: {query}.')
        logger.info(f'[Reflexion Memory]The summary response is: {summary}.')
        return summary
    
    def generate_insight(self, post_memory):
        query: str = f"""As an AI assistant, you are helping a six-year-old player who has never played this game before. The experiences you have are as follows:"""
        if len(post_memory) > 0:
            for i, m in enumerate(post_memory):
                query += f'Episode #{i}: {m}\n'
        query += '\n Identify and summarize the key information that can be exploited to improve performance of the player.'
        insight = get_chat(query,model=self.args.gpt_version, engine=self.args.gpt_version)
        # import pdb;pdb.set_trace()
        logger.info(f'[Reflexion Memory]The insight prompt is: {query}.')
        logger.info(f'[Reflexion Memory]The insight response is: {insight}.')
        return insight
    
    def generate_suggestion(self, game_description, goal_description, action_description, pre_memory, post_memory, insight, max_num_trials):
        query: str = f"""You are an AI assitant that help a human player win the following game.
        The game is \n"{game_description}" \n, the action space is described as {action_description},\n the player's goal is \n "{goal_description}".\n
        The player can play for {max_num_trials} episodes. The main aim for you is to help the player win the game in the last episode. """
        if len(post_memory) > 0:
            query +=  f"""You have obtained experience as below """
            for i, m in enumerate(post_memory):
                query += f'Episode #{i}: {m}\n'

        query += f"\n The main aim for you is to help the human player win the game in the last episode. He has only {max(max_num_trials-len(post_memory), 1)} episodes left to try.You can give suggestions before each episode. Then what is your suggestion for his next episode? Please provide simple, concise answers suitable for a six-year-old child, focusing on the following in item list format: 1. What game-relevant knowledge is critical to determine the optimal policy. Notice that the knowledge should be obtainable by interacting with the environment and helpful for the decisions.\n 2. How should the player conduct exploration in the next episode to acquire this information?\n3. How can the player exploit the information obtained to achieve higher performance in subsequent episodes?\n 4. How should exploration and exploitation be balanced to improve performance in the next episode?\n"

        # TODO: consider the inconsistency between past suggestion and past memory.
        suggestion = get_chat(query,model=self.args.gpt_version, engine=self.args.gpt_version)
        self.suggestion = suggestion
        logger.info(f'[Reflexion Memory]The suggestion prompt is: {query}.')
        logger.info(f'[Reflexion Memory]The suggestion response is: {suggestion}.')
        return suggestion
            
    def generate(self, traj, memory, max_len_mem=5):
        if len(memory)> max_len_mem:
            reflection_query = self._generate_summary_query(traj, memory[-max_len_mem:])
        else:
            reflection_query = self._generate_summary_query(traj, memory)
        reflection = get_completion(reflection_query,engine=self.args.gpt_version)
        logger.info(f'[Reflexion Memory]The reflexion prompt is: {reflection_query}.')
        logger.info(f'[Reflexion Memory]The reflexion response is: {reflection}.')
        return reflection
