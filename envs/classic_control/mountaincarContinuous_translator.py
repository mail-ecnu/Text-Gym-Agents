class BasicLevelTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        car_position, car_velocity = state
        car_direction = "right" if car_velocity > 0 else "left"
        res = (f"The car is positioned at {car_position:.3f}, with a velocity of {abs(car_velocity):.3f} towards the {car_direction}.")
       
        return res

class GameDescriber:
    def __init__(self, args):
        self.is_only_local_obs = args.is_only_local_obs == 1
        self.max_episode_len = args.max_episode_len
        self.action_desc_dict = {
        }
        self.reward_desc_dict = {
        }

    def describe_goal(self):
        return "The goal is to reach the flag placed on top of the right hill as quickly as possible."

    def translate_terminate_state(self, state, episode_len, max_episode_len): 
        return ""

    def translate_potential_next_state(self, state, action):
        return ""
        
    def describe_game(self):
        return ("In the Mountain Car game, you control a car placed stochastically at the bottom of a sinusoidal valley. "
                "The only possible actions are the accelerations between -1 and 1 that can be applied to the car in either direction. "
                "The goal of the game is to strategically accelerate the car to reach the goal state on top of the right hill "
                "as quickly as possible. The episode ends if either the car reaches the goal position on top of the right hill "
                f"or the length of the episode is {self.max_episode_len}.")

    def describe_action(self):
        return ("Type a numerical value within the range of [-1,1], which represents the directional force being applied to the car. The action will be limited to the range of [-1,1], and then multiplied by a power of 0.0015.")

class BasicStateSequenceTranslator(BasicLevelTranslator):
    def translate(self, infos, is_current=False):
        descriptions = []
        if is_current:
            state_desc = BasicLevelTranslator().translate(infos[-1]['state'])
            return state_desc
        for i, info in enumerate(infos):
            assert 'state' in info, "info should contain state information"

            state_desc = BasicLevelTranslator().translate(info['state'])
            action_desc = f"Take Action: ({info['action']})."
            reward_desc = f"Result: Reward of {info['reward']}, "
            next_state_desc = BasicLevelTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\n {action_desc} \n {reward_desc} \n Transit to {next_state_desc}")
        return descriptions
