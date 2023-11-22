import numpy as np
def dedicated_1_policy(state, pre_action=1):
    def get_description():   
        return "Always select action 1 which do nothing"
    dedicated_1_policy.description = get_description()
    return 1

def dedicated_2_policy(state, pre_action=1):
    def get_description():
        return "Always select action 2 which fire left engine"
    dedicated_2_policy.description = get_description()
    return 2

def dedicated_3_policy(state, pre_action=1):
    def get_description():
        return "Always select action 3 which fire main engine"
    dedicated_3_policy.description = get_description()
    return 3

def dedicated_4_policy(state, pre_action=1):
    def get_description():
        return "Always select action 4 which fire right engine"
    dedicated_4_policy.description = get_description()
    return 4

def pseudo_random_policy(state, pre_action):
    def get_description():
        return "Select action 1, 2, 3, 4 alternatively which do nothing, fire left engine, fire main engine, and fire right engine alternatively"
    pseudo_random_policy.description = get_description()
    return pre_action%4+1

def real_random_policy(state,pre_action=0):
    def get_description():
        return "Select action with a random policy"
    real_random_policy.description = get_description()
    return np.random.choice([1, 2, 3, 4])
