def sample_trajectory(env, policy, initial_state, max_steps=5):
    # Set the initial state
    env.set_state(initial_state)
    infos = []
    info = {}
    try: 
        pre_action = env.action_space.low 
    except: 
        pre_action = 0 
    # Sample the trajectory
    utility = 0 
    trajectory = []
    for i in range(max_steps):
        info['state'] = env.state['state']
        action = policy(env.state, pre_action)
        state, reward, done, _, _ = env.step_llm(action)
        info['action'] = action 
        info['reward'] = reward 
        info['next_state'] = state 
        info['terminated'] = done
        infos.append(info)
        info = {}
        utility += reward
        pre_action = action
        if done:
            break
    return infos, utility


def policy_based_translator(env, policy, state, summarizer, future_horizon=20):
    # Sample a trajectory using the policy
    trajectory, utility = sample_trajectory(env, policy, state, future_horizon)
    summary = {
        'policy description': policy.description, 
        'cummulative reward': utility, 
        'trajectory': summarizer.translate(trajectory)
    }
    return summary

def prefix_current(): 
    prefix = "Current Game State: \n"
    return prefix 

def prefix_future():
    prefix = "Potential Future of the Game."    
    return prefix 

class Translator(): 
    def __init__(self, init_summarizer, curr_summarizer, future_summarizer, env, horizon=1):
        self.init_summarizer = init_summarizer
        self.curr_summarizer = curr_summarizer
        self.future_summarizer = future_summarizer
        self.infos = [] 
        self.horizon = horizon
        self.env = env

    def obtain(self, info):
        self.infos.append(info)
        if len(self.infos) > self.horizon:
            self.infos.pop(0)
    
    def update(self, info):
        self.infos[-1] = info

    def translate(self,):
        if self.env:
            self.env.reset()
        summary = ""
        future_summary = []
        summary += self.curr_summarizer.translate(self.infos)
        if self.future_summarizer and self.env: 
            future_summary = self.future_summarizer.translate(self.env, self.infos)
        return summary, future_summary

    def translate_terminate_state(self, state, episode_len, max_episode_len): 
        return self.init_summarizer.translate_terminate_state(state, episode_len, max_episode_len)

    def translate_potential_next_state(self, state, action):
        return self.init_summarizer.translate_potential_next_state(state, action)
    def describe_game(self,):
        return self.init_summarizer.describe_game()

    def describe_goal(self,):
        return self.init_summarizer.describe_goal()
    
    def describe_action(self,):
        return self.init_summarizer.describe_action()

    def get_action_desc_dict(self,):
        return self.init_summarizer.get_action_desc_dict()

    def get_reward_desc_dict(self,):
        return self.init_summarizer.get_reward_desc_dict()

class InitSummarizer:
    def __init__(self, base_summarizer, args):
        self.summarizer = base_summarizer(args)

    def describe_game(self):
        return self.summarizer.describe_game()         
    
    def describe_goal(self):
        return self.summarizer.describe_goal()

    def describe_action(self):
        return self.summarizer.describe_action()

    def translate_terminate_state(self, state, episode_len, max_episode_len):
        return self.summarizer.translate_terminate_state(state, episode_len, max_episode_len)
    
    def translate_potential_next_state(self, state, action):
        return self.summarizer.translate_potential_next_state(state, action)
    
    def get_reward_desc_dict(self,):
        return self.summarizer.reward_desc_dict

    def get_action_desc_dict(self,):
        return self.summarizer.action_desc_dict

class CurrSummarizer():
    def __init__(self, base_summarizer):
        self.base_summarizer = base_summarizer()
        
    def translate(self, infos):
        summary = ""
        summary += prefix_current()
        summary += self.base_summarizer.translate([infos[-1]], is_current=True) 
        return summary 
    
class FutureSummarizer():
    def __init__(self, base_summarizer, policies, future_horizon=50):
        self.base_summarizer = base_summarizer()
        self.future_horizon = future_horizon
        self.policies = policies

    def translate(self, env, infos):
        # summary = prefix_future()
        future_info_dict = {'info_description': prefix_future()}
        for policy in self.policies: 
            future_info_dict[f'{policy.__name__}'] = policy_based_translator(env, policy, infos[-1], self.base_summarizer, future_horizon=self.future_horizon)
        return future_info_dict 
