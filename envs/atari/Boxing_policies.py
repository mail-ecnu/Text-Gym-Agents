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
        return "Select an action among 1 to 18 alternatively"
    pseudo_random_policy.description = get_description()
    return pre_action % 18 + 1


def real_random_policy(state, pre_action=1):
    def get_description():
        return "Select action with a random policy"

    real_random_policy.description = get_description()
    return np.random.choice(range(0, 18)) + 1


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

    dedicated_8.description = get_description()
    return 8


def dedicated_9_policy(state, pre_action=1):
    def get_description():
        return "Always select action 9 which moves the agent down and to the right"

    dedicated_9.description = get_description()
    return 9


def dedicated_10_policy(state, pre_action=1):
    def get_description():
        return "Always select action 10 which moves the agent down and to the left"

    dedicated_10_policy.description = get_description()
    return 10


def dedicated_11_policy(state, pre_action=1):
    def get_description():
        return "Always select action 11 which moves the agent up while hiting the enemy"

    dedicated_11_policy.description = get_description()
    return 11


def dedicated_12_policy(state, pre_action=1):
    def get_description():
        return "Always select action 12 which moves the agent right while hiting the enemy"

    dedicated_12_policy.description = get_description()
    return 12


def dedicated_13_policy(state, pre_action=1):
    def get_description():
        return "Always select action 13 which moves the agent left while hiting the enemy"

    dedicated_13_policy.description = get_description()
    return 13


def dedicated_14_policy(state, pre_action=1):
    def get_description():
        return "Always select action 14 which moves the agent down while hiting the enemy"

    dedicated_14_policy.description = get_description()
    return 14


def dedicated_15_policy(state, pre_action=1):
    def get_description():
        return "Always select action 15 which moves the agent up and to the right while hiting the enemy"

    dedicated_15_policy.description = get_description()
    return 15


def dedicated_16_policy(state, pre_action=1):
    def get_description():
        return "Always select action 16 which moves the agent up and to the left while hiting the enemy"

    dedicated_16_policy.description = get_description()
    return 16


def dedicated_17_policy(state, pre_action=1):
    def get_description():
        return "Always select action 17 which moves the agent down and to the right while hiting the enemy"

    dedicated_17_policy.description = get_description()
    return 17


def dedicated_18_policy(state, pre_action=1):
    def get_description():
        return "Always select action 18 which moves the agent down and to the left while hiting the enemy"

    dedicated_18_policy.description = get_description()
    return 18
