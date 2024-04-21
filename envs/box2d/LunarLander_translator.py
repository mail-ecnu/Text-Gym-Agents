# [Translator classes and functions for Lunar Lander environment]

class BasicLevelTranslator:
    def __init__(self,):
        pass

    def translate(self, state):
        x, y, x_dot, y_dot, angle, angular_velocity, left_leg_contact, right_leg_contact = state
        left_contact_info = "in contact" if left_leg_contact else "not in contact"
        right_contact_info = "in contact" if right_leg_contact else "not in contact"
        return f"The lander is at position ({x:.2f}, {y:.2f}), the horizontal speed of movement is {x_dot:.2f}, " \
               f"the vertical velocity speed of movement is {y_dot:.2f}. The angle is {angle:.2f} radians, and it's rotating at {angular_velocity:.2f} radians per second. The left leg is {left_contact_info} with ground. The right leg is {right_contact_info} with ground."

class GameDescriber:
    def __init__(self, args):
        self.is_only_local_obs = args.is_only_local_obs == 1
        self.max_episode_len = args.max_episode_len
        self.action_desc_dict = {
        }
        self.reward_desc_dict = {
        }
        
    def describe_goal(self):
        return "The goal is to successfully land the lander on the landing pad which is at position (0, 0) while avoiding crash."

    def translate_terminate_state(self, state, episode_len, max_episode_len): 
        return ""
        
    def translate_potential_next_state(self, state, action):
        return ""
        
    def describe_game(self):
        return "In the Lunar Lander game, you control a lander that is descending towards " \
               "the landing pad. The goal is to successfully land the lander on the landing pad " \
               "while avoiding crash. Please note that the lander is affected by gravity, and the lander starts at the " \
               "top center of the viewport with a random initial force applied to its center of mass. " \
               "Be careful to balance the engine to slow down your descent " \
               "and land gently. If you land too quickly or crash into the landing pad, the game will " \
               "end, and you will be punished."
    
    def describe_action(self):
        return "Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, " \
               "or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4]."


class BasicStateSequenceTranslator(BasicLevelTranslator):
    def translate(self, infos, is_current=False):
        descriptions = []
        if is_current: 
            state_desc = BasicLevelTranslator().translate(infos[-1]['state'])
            return state_desc
        for i, info in enumerate(infos):
            assert 'state' in info, "info should contain state information"
        
            state_desc = BasicLevelTranslator().translate(info['state'])
            if info['action'] == 1:
                action_desc = f"Take Action: 'Do Noting'"
            elif info['action'] == 2:
                action_desc = f"Take Action: 'Fire left engine'"
            elif info['action'] == 3:
                action_desc = f"Take Action: 'Fire main engine'"
            else:
                action_desc = f"Take Action: 'Fire right engine'"
            reward_desc = f"Result: Reward of {info['reward']}, "
            next_state_desc = BasicLevelTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\n {action_desc} \n {reward_desc} \n Transit to {next_state_desc}")
        return descriptions
