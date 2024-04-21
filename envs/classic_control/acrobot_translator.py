import math

class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        cos_theta1, sin_theta1, cos_theta2, sin_theta2, theta1_dot, theta2_dot = state
        theta1_direction = "clockwise" if theta1_dot > 0 else "counterclockwise"
        theta2_direction = "clockwise" if theta2_dot > 0 else "counterclockwise"
        theta1 = math.atan(sin_theta1 / (cos_theta1+1e-6))
        theta2 = math.atan(sin_theta2 / (cos_theta2+1e-6))
        res = (f"Link1: angle theta1 {theta1:.2f} radians, rotating {abs(theta1_dot):.2f} radians per second {theta1_direction}. "
               f"Link2: angle theta2 {theta2:.2f} radians relative to Link1, rotating {abs(theta2_dot):.2f} radians per second {theta2_direction}.")
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
        return "The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0."

    def translate_terminate_state(self, state, episode_len, max_episode_len): 
        return ""
    
    def translate_potential_next_state(self, state, action):
        return ""
        
    def describe_game(self):
        return ('''In the Acrobot game, there are two links connected by two joints. The first link is connected to a base, and your goal is to swing the free end of the second link above the target height by applying torques on the actuated joint. The task ends if one of the following occurs: 1. The free end reaches the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0; or 2. Decision time is greater than 200.''')

    # https://colab.research.google.com/drive/1DdWsGi10232orUv-reY4wsTmT0VMoHaX?usp=sharing#scrollTo=4OfVmDKk7XvG
    # LLMs bias on 0 so make the actions 1, 2 and 3 instead.
    def describe_action(self):
        return ("Type '1' to apply -1 torque, '2' to apply 0 torque, or '3' to apply 1 torque. "
                "Ensure you provide the action number from the valid action list, i.e., [1, 2, 3].")

class TransitionTranslator(ObsTranslator):
    def translate(self, infos, is_current=False):
        descriptions = []
        if is_current:
            state_desc = ObsTranslator().translate(infos[-1]['state'])
            return state_desc
        for i, info in enumerate(infos):
            assert 'state' in info, "info should contain state information"

            state_desc = ObsTranslator().translate(info['state'])
            action_desc = f"Take Action: Apply {info['action'] - 2} torque on the actuated joint."
            reward_desc = f"Result: Reward of {info['reward']}."
            next_state_desc = ObsTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\n {action_desc} \n {reward_desc} \n Transit to {next_state_desc}")
        return descriptions
