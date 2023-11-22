import numpy as np

# https://colab.research.google.com/drive/1DdWsGi10232orUv-reY4wsTmT0VMoHaX?usp=sharing#scrollTo=4OfVmDKk7XvG
# LLMs bias on 0 so make the actions 1, 2 and 3 instead.

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

def dedicated_3_policy(state, pre_action=1):
    def get_description():
        return "Always select action 3"
    dedicated_3_policy.description = get_description()
    return 3

def pseudo_random_policy(state, pre_action):
    def get_description():
        return "Select action 1, 2, and 3 alternatively"
    pseudo_random_policy.description = get_description()
    return pre_action % 3 + 1


def real_random_policy(state, pre_action=1):
    def get_description():
        return "Select action with a random policy"
    real_random_policy.description = get_description()
    return np.random.choice([0, 1, 2])

