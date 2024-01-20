from typing import List, Dict


class EnvironmentHistory:
    def __init__(self, ) -> None:
        self._history = []
    
    def add(self, label: str, value: str) -> None:
        assert label in ['action', 'observation', 'human_edit', 'reward', 'cummulative_reward', 'terminate_state']
        self._history += [{
            'label': label,
            'value': value,
        }]

    def reset(self) -> None:
        self._history = []

    def __str__(self) -> str:
        s = ''
        for i, item in enumerate(self._history):
            if item['label'] == 'action':
                s += f'He takes action: {item["value"]}'
            elif item['label'] == 'observation':
                s += item['value']
            elif item['label'] == 'reward':
                s += f'{item["value"]}'
            elif item['label'] == 'cummulative_reward':
                s += f'Performance: {item["value"]}'
            # NOT CURRENTLY SUPPORTED
            elif item['label'] == 'human_edit':
                s += f'[human edit]: {item["value"]}'
            elif item['label'] == 'terminate_state':
                s += f'{item["value"]}'
            if i != len(self._history) - 1:
                s += '\n'
        return s
    
    def get_one_history(self) -> str:
        s = ''
        elements = set([ele['label'] for ele in self._history])
        elements.discard('cummulative_reward')
        state_num = len(elements)
        for i, item in enumerate(self._history[:state_num]):
            if item['label'] == 'action':
                s += f'He takes action: {item["value"]}'
            elif item['label'] == 'reward':
                s += f'{item["value"]}'
            elif item['label'] == 'cummulative_reward':
                s += f'Performace: {item["value"]}'
            elif item['label'] == 'observation':
                s += item['value']
            # NOT CURRENTLY SUPPORTED
            elif item['label'] == 'human_edit':
                s += f'[human edit]: {item["value"]}'
            elif item['label'] == 'terminate_state':
                s += f'{item["value"]}'
            if i != len(self._history) - 1:
                s += '\n'
        return s
    
    def set_history(self, num):
        if len(self._history) > num:
            # print(self._history,num)
            self._history = self._history[-num:]

    def get_last_history(self) -> str:
        s = ''
        for i, item in enumerate(self._history[-1:]):
            if item['label'] == 'action':
                s += f'He takes action: {item["value"]}'
            elif item['label'] == 'reward':
                s += f'{item["value"]}'
            elif item['label'] == 'cummulative_reward':
                s += f'Performace: {item["value"]}'
            elif item['label'] == 'observation':
                s += item['value']
            # NOT CURRENTLY SUPPORTED
            elif item['label'] == 'human_edit':
                s += f'[human edit]: {item["value"]}'
            elif item['label'] == 'terminate_state':
                s += f'{item["value"]}'
            if i != len(self._history) - 1:
                s += '\n'
        return s
    
    def get_histories(self,num):
        s = ''
        state_num = 0
        elements = set([ele['label'] for ele in self._history])
        elements.discard('cummulative_reward')
        state_num = len(elements)
        history_num = state_num*num+1
        for i, item in enumerate(self._history[-history_num:-1]):
            if item['label'] == 'action':
                s += f'He takes action: {item["value"]}'
            elif item['label'] == 'reward':
                s += f'{item["value"]}'
            elif item['label'] == 'cummulative_reward':
                s += f'Performace: {item["value"]}'
            elif item['label'] == 'observation':
                s += item['value']
            # NOT CURRENTLY SUPPORTED
            elif item['label'] == 'human_edit':
                s += f'[human edit]: {item["value"]}'
            elif item['label'] == 'terminate_state':
                s += f'{item["value"]}'
            if i != len(self._history) - 1:
                s += '\n'
        return s
    
    def get_histories_with_last(self,num):
        s = ''
        state_num = 0
        elements = set([ele['label'] for ele in self._history])
        elements.discard('cummulative_reward')
        state_num = len(elements)
        history_num = state_num*num+1
        for i, item in enumerate(self._history[-history_num:]):
            if item['label'] == 'action':
                s += f'He takes action: {item["value"]}'
            elif item['label'] == 'reward':
                s += f'Reward after taking action: {item["value"]}'
            elif item['label'] == 'cummulative_reward':
                s += f'Performace: {item["value"]}'
            elif item['label'] == 'observation':
                s += item['value']
            # NOT CURRENTLY SUPPORTED
            elif item['label'] == 'human_edit':
                s += f'[human edit]: {item["value"]}'
            elif item['label'] == 'terminate_state':
                s += f'{item["value"]}'
            if i != len(self._history) - 1:
                s += '\n'
        return s

    def get_lastest_histories_list(self, num):
        s = ''
        state_num = 0
        elements = set([ele['label'] for ele in self._history])
        elements.discard('cummulative_reward')
        state_num = len(elements)
        history_num = state_num*num+1
        history_list = []
        for i, item in enumerate(self._history):
            if item['label'] == 'action':
                s += f'He takes action: {item["value"]}'
            elif item['label'] == 'reward':
                s += f'Reward after taking action: {item["value"]}'
            elif item['label'] == 'cummulative_reward':
                s += f'Performace: {item["value"]}'
            elif item['label'] == 'observation':
                s += item['value']
            # NOT CURRENTLY SUPPORTED
            elif item['label'] == 'human_edit':
                s += f'[human edit]: {item["value"]}'
            elif item['label'] == 'terminate_state':
                s += f'{item["value"]}'
            if (i+1) % history_num == 0 or i == len(self._history) - 1:
                history_list.append(s)
                s = ''
        return history_list
        
    def remove_invalid_state(self):
        self._history = self._history[:-1]

    def __len__(self) -> int:
        action = [item for item in self._history if item['label'] == 'action' ]
        return len(action)
