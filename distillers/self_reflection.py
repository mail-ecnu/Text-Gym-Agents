from deciders.utils import get_chat, num_tokens_from_string

from typing import List, Dict, Any
from loguru import logger
import random 
import json
class ReflectionGenerator():
    def __init__(self,logfile="",args=None):
        self.args = args
        self.seed = args.seed
        with open("./distillers/reflexion_few_shot_examples.txt", 'r') as f:
            self.FEW_SHOT_EXAMPLES = f.read()
        if logfile:
            # logger.remove()
            logger.add(logfile, colorize=True, enqueue=True, filter=lambda x: '[Reflexion Memory]' in x['message'])

    def generate_from_file(self, client,  file_path,max_step_num=200):
        mem = []
        with open(file_path, 'r') as infile:
            data = json.load(infile)

        traj_lst = []
        for traj in data: 
            game_description = traj[0]['game_description']
            goal_description = traj[0]['goal_description']
            action_description = traj[0]['action_description']

            traj_text = ""
            for transition in traj[-max_step_num:]: 
                traj_text += transition['observation']+'\n'
                if type(eval(str(transition['action']))) == type([]):
                    action = float(eval(str(transition['action']))[0])-1
                else:
                    action = transition['action']
                traj_text += f"Action: {action}\n"
                traj_text += f"Reward: {transition['reward']}\n"
                if num_tokens_from_string(self.args.gpt_version, traj_text) > 0.3*self.args.max_query_tokens:
                    traj_lst.append(traj_text)
                    traj_text = ""
            traj_text += f"Your performance is: {transition['cum_reward']}\n"

            traj_lst.append(traj_text)
            reflection = self.generate(client, traj_lst, mem, game_description, goal_description, action_description, max_len_mem=5)
            mem.append(reflection)
        return mem

    def _generate_reflection_query(self, traj_lst, memory, game_description, goal_description, action_description):
        """Allows the Agent to reflect upon a past experience."""
        messages = []
        messages.append({"role": "system",  "content": """ You will be given the history of a past experience in which you were placed in an environment and given a task to complete. You were unsuccessful in completing the task. Do not summarize your environment, but rather think about the strategy and path you took to attempt to complete the task. Think step by step what mistakes you made leading the failure. Then devise a concise, new plan of action that accounts for your mistake with reference to specific actions that you should have taken. For example, if you tried A and B but forgot C, then you should reason that the forgetting C is the key mistake. After that you devise a plan to achieve C with environment-specific actions. You remind yourself the plan your will take in the next trail and Give your plan after "Plan". """})
        messages.append({"role": "system", "name": "example_assitant", "content": self.FEW_SHOT_EXAMPLES})
    
        messages.append({"role": "system", "content": f"You are in a game. {game_description} \n {goal_description} \n {action_description}" })
        if len(memory) > 0:
            for i, m in enumerate(memory):
                query = f'Recent Plans. Trial #{i}: {m}\n'
                messages.append({"role": "system", "name": "previous_assistant", "content": query})
        i_traj = 0 
        for traj in traj_lst:
            if i_traj == 0:
                query = f'Your previous trajectory is: {traj}\n'
            else:
                query = traj
            messages.append({"role": "user", "content": query})
            i_traj += 1
        for i in range(len(messages)):
            if num_tokens_from_string(self.args.gpt_version, messages[:i]) > 0.98*self.args.max_query_tokens:
                messages = messages[:i-1]
                break
        messages.append({"role": "user", "content": "Please give your new plan"})
        
        return messages

    def generate(self, client, traj_lst, memory, game_description, goal_description, action_description, max_len_mem=5):
        if len(memory)> max_len_mem:
            reflection_messages = self._generate_reflection_query(traj_lst, memory[-max_len_mem:], game_description, goal_description, action_description)
        else:
            reflection_messages = self._generate_reflection_query(traj_lst, memory, game_description, goal_description, action_description)
        reflection, relfexion_usage = get_chat(reflection_messages, api_type=self.args.api_type,  seed=self.seed, model=self.args.gpt_version)
        logger.info(f'[Reflexion Memory]The reflexion prompt is: {reflection_messages}.')
        logger.info(f'[Reflexion Memory]The reflexion response is: {reflection}.')
        logger.info(f'[Reflexion Memory]The reflexion usage is: {relfexion_usage}.')
        return reflection
