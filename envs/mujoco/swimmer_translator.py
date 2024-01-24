'''Swimmer
Action Space Box(-1.0, 1.0, (2,), float32)

Observation Space Box(-inf, inf, (8,), float64)
'''

class ObsTranslator:
    def translate(self, state):
        res = (
            f"Angle of the front tip: {state[0]:.2f} rad\n"
            f"Angle of the first rotor: {state[1]:.2f} rad\n"
            f"Angle of the second rotor: {state[2]:.2f} rad\n"
            f"Velocity of the tip along the x-axis: {state[3]:.2f} m/s\n"
            f"Velocity of the tip along the y-axis: {state[4]:.2f} m/s\n"
            f"Angular velocity of front tip: {state[5]:.2f} rad/s\n"
            f"Angular velocity of the first rotor: {state[6]:.2f} rad/s\n"
            f"Angular velocity of the second rotor: {state[7]:.2f} rad/s"
        )
        return res

class GameDescriber:

    def __init__(self, args):
        self.is_only_local_obs = args.is_only_local_obs == 1
        self.max_episode_len = args.max_episode_len
        self.action_desc_dict = {
        }
        self.reward_desc_dict = {
        }
    
    def translate_terminate_state(self, state, episode_len, max_episode_len): 
        return ""
        
    def translate_potential_next_state(self, state, action):
        return ""

    def describe_goal(self):
        return (
            "The goal in the Swimmer environment is to move as fast as possible towards the right "\
            "by applying torque to the rotors and utilizing fluid friction. The swimmer consists of "\
            "three or more segments connected by rotors, and the objective is to achieve efficient "\
            "swimming motion."
        )

    def describe_game(self):
        return (
            "In the Swimmer environment, you control a swimmer consisting of three or more segments "\
            "connected by rotors. Your goal is to make the swimmer move as fast as possible to the right "\
            "in a two-dimensional pool. You can achieve this by applying torques to the rotors and utilizing "\
            "fluid friction. The environment provides observations of the swimmer's angles, velocities, "\
            "and angular velocities."
        )

    def describe_action(self):
        return (
            "Your next move: \nPlease provide a list of two numerical values, each within the range of [-1, 1], "\
            "representing the torques to be applied to the two rotors of the swimmer. These torques will help "\
            "control the swimmer's movement and achieve efficient swimming."
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
            action_desc = (
                "Torques Applied: "
                f"Rotor 1: {info['action'][0]:.2f}, Rotor 2: {info['action'][1]:.2f}"
            )
            reward_desc = f"Result: Reward of {info['reward']:.2f}"
            next_state_desc = ObsTranslator().translate(info['next_state'])
            descriptions.append(
                f"{state_desc}\n{action_desc}\n{reward_desc}\nTransit to\n{next_state_desc}"
            )
        return descriptions
