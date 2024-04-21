
class BasicLevelTranslator:
    def __init__(self,):
        pass

    def translate(self, state):
        cart_position, cart_velocity, pole_angle, pole_angular_velocity = state
        cart_direction = "right" if cart_velocity > 0 else "left"
        pole_direction = "right" if pole_angular_velocity > 0 else "left"
        res = (f"The cart is positioned at {cart_position:.3f}, with a velocity of {abs(cart_velocity):.2f} towards the {cart_direction}. "
                f"The pole is tilted at {abs(pole_angle):.2f} radians, rotating at {abs(pole_angular_velocity):.2f} radians per second towards the {pole_direction}.")
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
        return "The goal is to keep the pole balanced upright for as long as possible."

    def translate_terminate_state(self, state, episode_len, max_episode_len): 
        return ""

    def translate_potential_next_state(self, state, action):
        return ""
        
    def describe_game(self):
        return "In the CartPole game, you control a cart that moves along a horizontal track. There is a pole " \
               "standing upright on the cart. The goal of the game is to keep the pole balanced upright by moving the " \
               "cart left or right. The game ends if the pole tilts too far from the vertical position or if the cart " \
               "moves too far from the center of the track. The longer you can keep the pole balanced, the higher " \
               "your score.Note that when the Cart Position is out of the (-2.4, 2.4) zone or the Pole Angle is out " \
               "of the zone (-.2095, .2095), the round ends and the game is lost. "
    
    def describe_action(self):
        return "Type '1' to push the cart to the left or '2' to push the cart to the right. Ensure you only provide the action number from the valid action list, i.e., [1, 2]."

class BasicStateSequenceTranslator(BasicLevelTranslator):
    def translate(self, infos, is_current=False):
        descriptions = []
        if is_current: 
            state_desc = BasicLevelTranslator().translate(infos[-1]['state'])
            return state_desc
        for i, info in enumerate(infos):
            assert 'state' in info, "info should contain state information"
        
            state_desc = BasicLevelTranslator().translate(info['state'])
            action_desc = f"Take Action: Push {'right' if info['action'] == 2 else 'left'} ({info['action']})."
            reward_desc = f"Result: Reward of {info['reward']}, "
            next_state_desc = BasicLevelTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\n {action_desc} \n {reward_desc} \n Transit to {next_state_desc}")
        return descriptions