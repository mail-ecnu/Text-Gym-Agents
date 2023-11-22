import random 
import json
class RawPromptGenerator():
    def __init__(self,args=None):
        self.args = args
        pass 
    
    def generate_from_file(self, file_path, choice_num=1):
        with open(file_path, 'r') as infile:
            data = json.load(infile)
        result = []
        for my_data in data[0]: 
            result.append({'question': my_data['question'], 'answer': my_data['answer']})
        selected_index = random.sample(range(len(result)), choice_num) 
        selected_result = [result[index] for index in selected_index]
        return selected_result