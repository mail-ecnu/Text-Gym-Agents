'''InvertedDoublePendulum-v4
Action Space Box(-1.0, 1.0, (1,), float32)
Observation Space Box(-inf, inf, (11,), float64)
'''

class ObsTranslator:
    def translate(self, state):
        res = (
            f"Position of the cart: {state[0]:.2f} m\n"
            f"Sine of the angle between cart and first pole: {state[1]:.2f}\n"
            f"Sine of the angle between two poles: {state[2]:.2f}\n"
            f"Cosine of the angle between cart and first pole: {state[3]:.2f}\n"
            f"Cosine of the angle between two poles: {state[4]:.2f}\n"
            f"Velocity of the cart: {state[5]:.2f} m/s\n"
            f"Angular velocity of angle between cart and first pole: {state[6]:.2f} rad/s\n"
            f"Angular velocity of angle between two poles: {state[7]:.2f} rad/s\n"
            f"Constraint Force 1: {state[8]:.2f} N\n"
            f"Constraint Force 2: {state[9]:.2f} N\n"
            f"Constraint Force 3: {state[10]:.2f} N"
        )
        return res

class GameDescriber:
    def __init__(self, args):
        self.is_only_local_obs = args.is_only_local_obs == 1
        self.max_episode_len = args.max_episode_len
        self.action_desc_dict = {
            0: "Apply a force in the range [-3, 3] to the cart to control its motion.",
        }
        self.reward_desc_dict = {}
    
    def translate_terminate_state(self, state, episode_len, max_episode_len):
        return ""
        
    def translate_potential_next_state(self, state, action):
        return ""
    
    def describe_goal(self):
        return (
            "The goal in the InvertedDoublePendulum environment is to balance the two poles "\
            "on top of the cart by applying continuous forces on the cart."
        )

    def describe_game(self):
        return (
            "In the InvertedDoublePendulum environment, you control a system with a cart and two poles. "\
            "Your objective is to balance the two poles on top of the cart by applying continuous forces "\
            "to the cart. The environment provides observations of the cart's position, angles of the poles, "\
            "and their angular velocities. The episode ends when certain termination conditions are met."
        )

    def describe_action(self):
        return (
            "Your next move: \n Please provide a numerical value within the range of [-3,3], "\
            "representing the force to be applied to the cart."
        )

class TransitionTranslator(ObsTranslator):
    def translate(self, infos, is_current=False):
        descriptions = []
        if is_current:
            state_desc = ObsTranslator().translate(infos[-1]['state'])
            return state_desc
        for i, info in enumerate(infos):
            assert 'state' in info, "info should contain state information"
            state_desc = ObsTranslator().translate(info['state'])
            action_desc = f"Applied Force on Cart: {info['action'][0]:.2f}"
            reward_desc = f"Result: Reward of {info['reward']:.2f}"
            next_state_desc = ObsTranslator().translate(info['next_state'])
            descriptions.append(
                f"{state_desc}\n{action_desc}\n{reward_desc}\nTransit to\n{next_state_desc}"
            )
        return descriptions