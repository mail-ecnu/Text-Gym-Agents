import numpy as np


def dedicated_1_policy(state, pre_action=1):
    def get_description():
        return "Always select action 1 which does NOOP (no operation)"

    dedicated_1_policy.description = get_description()
    return 1


def dedicated_2_policy(state, pre_action=1):
    def get_description():
        return "Always select action 2 which hits the enemy"

    dedicated_1_policy.description = get_description()
    return 2


def dedicated_3_policy(state, pre_action=1):
    def get_description():
        return "Always select action 3 which moves the agent up"

    dedicated_3_policy.description = get_description()
    return 3


def dedicated_4_policy(state, pre_action=1):
    def get_description():
        return "Always select action 4 which moves the agent right"

    dedicated_4_policy.description = get_description()
    return 4


def dedicated_5_policy(state, pre_action=1):
    def get_description():
        return "Always select action 5 which moves the agent left"

    dedicated_5_policy.description = get_description()
    return 5


def pseudo_random_policy(state, pre_action):
    def get_description():
        return "Select an action among 1 to 9 alternatively"
    pseudo_random_policy.description = get_description()
    return pre_action % 9 + 1


def real_random_policy(state, pre_action=1):
    def get_description():
        return "Select action with a random policy"
    real_random_policy.description = get_description()
    return np.random.choice(range(0, 9)) + 1


# Complete set of dedicated action policies
def dedicated_6_policy(state, pre_action=1):
    def get_description():
        return "Always select action 6 which moves the agent down"

    dedicated_6_policy.description = get_description()
    return 6


def dedicated_7_policy(state, pre_action=1):
    def get_description():
        return "Always select action 7 which moves the agent up and to the right"

    dedicated_7_policy.description = get_description()
    return 7


def dedicated_8_policy(state, pre_action=1):
    def get_description():
        return "Always select action 8 which moves the agent up and to the left"

    dedicated_8_policy.description = get_description()
    return 8


def dedicated_9_policy(state, pre_action=1):
    def get_description():
        return "Always select action 9 which moves the agent down and to the right"

    dedicated_9_policy.description = get_description()
    return 9