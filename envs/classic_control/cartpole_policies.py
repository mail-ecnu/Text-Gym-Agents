import numpy as np
def dedicated_1_policy(state, pre_action=1):
    def get_description():   
        return "Always select action 1"
    dedicated_1_policy.description = get_description()
    return 1

def dedicated_2_policy(state, pre_action=1):
    def get_description():
        return "Always select action 2"
    dedicated_2_policy.description = get_description()
    return 2

def pseudo_random_policy(state, pre_action):
    def get_description():
        return "Select action 1 and 2 alternatively"
    pseudo_random_policy.description = get_description()
    return pre_action%2 +1

def real_random_policy(state,pre_action=1):
    def get_description():
        return "Select action with a random policy"
    real_random_policy.description = get_description()
    return np.random.choice([1, 2])

