import numpy as np
import random

def pseudo_random_policy(state, pre_action):
    def get_description():
        return "Select action randomly"
    pseudo_random_policy.description = get_description()
    return 2 * random.random() - 1


def real_random_policy(state, pre_action=1):
    def get_description():
        return "Select action with a random policy"
    real_random_policy.description = get_description()
    return 2 * random.random() - 1

