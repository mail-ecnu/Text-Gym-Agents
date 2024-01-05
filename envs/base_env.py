# This file contains functions for interacting with the CartPole environment

import gym
from gym.spaces import Discrete

class SettableStateEnv(gym.Wrapper):
    def __init__(self, env):
        super().__init__(env)
        self.env = env

    def set_state(self, state):
        self.env.state = state
        self.env.steps_beyond_terminated = None

class BaseEnv(gym.Wrapper):
    def __init__(self, env, translator):
        super().__init__(env)
        self.translator = translator
        self.env_name = super().spec.id
        self.transition_data = {}
        self.game_description = self.get_game_description()
        self.goal_description = self.get_goal_description()
        self.action_description = self.get_action_description()
        self.action_desc_dict = self.get_action_desc_dict()
        self.reward_desc_dict = self.get_reward_desc_dict()

    def reset(self, **kwargs):
        state, _ = super().reset(**kwargs)
        self.transition_data['state'] = state
        self.translator.obtain(self.transition_data)
        summary, future_summary = self.translator.translate()
        info = {
            'future_summary': future_summary
        }
        self.state = state
        return summary, info

    def step(self, action): 
        potential_next_state = self.get_potential_next_state(action)
        state, reward, terminated, _, info = super().step(action)
        self.transition_data['action'] = action
        self.transition_data['next_state'] = state
        self.transition_data['reward'] = reward 
        self.transition_data['terminated'] = terminated
        self.translator.update(self.transition_data)
        self.transition_data = {}
        self.transition_data['state'] = state
        self.translator.obtain(self.transition_data)
        summary, future_summary = self.translator.translate()
        info = {
            'future_summary': future_summary,
            'potential_state': potential_next_state
        }
        return summary, reward, terminated, _, info


    def step_llm(self, action): 
        potential_next_state = self.get_potential_next_state(action)
        if isinstance(self.action_space, Discrete):
            state, reward, terminated, _, info = super().step(action-1)
        else:
            state, reward, terminated, _, info = super().step(action)
            
        self.transition_data['action'] = action
        self.transition_data['next_state'] = state
        self.transition_data['reward'] = reward 
        self.transition_data['terminated'] = terminated
        self.translator.update(self.transition_data)
        self.transition_data = {}
        self.transition_data['state'] = state
        self.translator.obtain(self.transition_data)
        self.state = state
        summary, future_summary = self.translator.translate()
        info = {
            'future_summary': future_summary,
            'potential_state': potential_next_state,
        }
        return summary, reward, terminated, _, info

    def get_terminate_state(self, episode_len, max_episode_len):
        return self.translator.translate_terminate_state(self.state, episode_len, max_episode_len)

    def get_game_description(self,):
        return self.translator.describe_game()

    def get_goal_description(self,):
        return self.translator.describe_goal()
    
    def get_action_description(self,):
        return self.translator.describe_action()

    def get_action_desc_dict(self,):
        return self.translator.get_action_desc_dict()

    def get_reward_desc_dict(self,):
        return self.translator.get_reward_desc_dict()

    def get_potential_next_state(self, action):
        return self.translator.translate_potential_next_state(self.state, action)