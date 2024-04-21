'''InvertedPendulum-v4
Action Space Box(-3.0, 3.0, (1,), float32)
Observation Space Box(-inf, inf, (4,), float64)
'''

class BasicLevelTranslator:
    def translate(self, state):
        res = (
            f"Position of the cart: {state[0]:.2f} m\n"
            f"Vertical angle of the pole: {state[1]:.2f} rad\n"
            f"Linear velocity of the cart: {state[2]:.2f} m/s\n"
            f"Angular velocity of the pole: {state[3]:.2f} rad/s"
        )
        return res

class GameDescriber:
    def __init__(self, args):
        self.is_only_local_obs = args.is_only_local_obs == 1
        self.max_episode_len = args.max_episode_len
        self.action_desc_dict = {
            0: "Apply a force in the range [-1, 1] to the cart to control its motion.",
        }
        self.reward_desc_dict = {}
    
    def translate_terminate_state(self, state, episode_len, max_episode_len):
        return ""
        
    def translate_potential_next_state(self, state, action):
        return ""
    
    def describe_goal(self):
        return (
            "The goal in the Inverted Pendulum environment is to balance the pole on top of the cart "\
            "by applying continuous forces to the cart, keeping it upright."
        )

    def describe_game(self):
        return (
            "In the Inverted Pendulum environment, you control a cart that can move linearly with a pole "\
            "attached to it. Your objective is to balance the pole on top of the cart by applying forces "\
            "to the cart in a way that keeps the pole upright. "\
            "The environment provides observations of the cart's position, pole angle, velocities, "\
            "and angular velocities. The goal is to maintain balance as long as possible."
        )

    def describe_action(self):
        return (
            "Type a numerical value for the force to be applied to the cart. "\
            "This value should be within the range of [-3, 3], where a positive value indicates applying force "\
            "in the right direction, and a negative value indicates applying force in the left direction."
        )

class BasicStateSequenceTranslator(BasicLevelTranslator):
    def translate(self, infos, is_current=False):
        descriptions = []
        if is_current:
            state_desc = BasicLevelTranslator().translate(infos[-1]['state'])
            return state_desc
        for i, info in enumerate(infos):
            assert 'state' in info, "info should contain state information"
            state_desc = BasicLevelTranslator().translate(info['state'])
            action_desc = f"Applied Force on Cart: {info['action'][0]:.2f}"
            reward_desc = f"Result: Reward of {info['reward']:.2f}"
            next_state_desc = BasicLevelTranslator().translate(info['next_state'])
            descriptions.append(
                f"{state_desc}\n{action_desc}\n{reward_desc}\nTransit to\n{next_state_desc}"
            )
        return descriptions