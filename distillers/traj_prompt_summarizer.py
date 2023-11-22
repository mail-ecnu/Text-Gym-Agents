import random 
from deciders.utils import get_completion
import json
class TrajPromptSummarizer():
    def __init__(self,args=None):
        self.args = args
        with open("./distillers/traj_summary_few_shot_examples.txt", 'r') as f:
            self.FEW_SHOT_EXAMPLES = f.read()

    def generate_from_file(self, file_path,max_step_num=200):
        mem = []
        with open(file_path, 'r') as infile:
            data = json.load(infile)
        for traj in data: 
            traj_text = traj[0]['game_description']
            traj_text += traj[0]['goal_description']
            for transition in traj[-max_step_num:]: 
                traj_text += transition['observation']
                traj_text += f"> {transition['action']}"
            traj_text += f"Your performance is: {transition['cum_reward']}"
            reflection = self.generate(traj_text, mem, max_len_mem=5)
            mem.append(reflection)        
        return mem

    def _generate_summary_query(self, traj, memory):
        """Allows the Agent to reflect upon a past experience."""
        query: str = f"""You will be given the history of a past experience in which you were placed in an environment and given a task to complete. Summarize your trajectory and reasoning the relation between your policy and the obtained result. Here are two examples:

        {self.FEW_SHOT_EXAMPLES}

        {traj}"""
        if len(memory) > 0:
            query += '\n\nPlans from past attempts:\n'
            for i, m in enumerate(memory):
                query += f'Trial #{i}: {m}\n'

        query += '\n\nSummary:'
        return query

    def generate(self, traj, memory, max_len_mem=5):
        if len(memory)> max_len_mem:
            reflection_query = self._generate_summary_query(traj, memory[-max_len_mem:])
        else:
            reflection_query = self._generate_summary_query(traj, memory)
        reflection = get_completion(reflection_query, engine=self.args.gpt_version) 
        return reflection