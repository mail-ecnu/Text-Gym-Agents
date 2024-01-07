
'''Walker2d
Action Space Box(-1.0, 1.0, (6,), float32)
Observation Space Box(-inf, inf, (17,), float64)
'''
class BasicLevelTranslator:
    def translate(self, state):
        res = (
            f"Z-coordinate of the top (height of walker): {state[0]:.2f} m\n"
            f"Angle of the top: {state[1]:.2f} rad\n"
            f"Angle of the thigh joint: {state[2]:.2f} rad\n"
            f"Angle of the leg joint: {state[3]:.2f} rad\n"
            f"Angle of the foot joint: {state[4]:.2f} rad\n"
            f"Angle of the left thigh joint: {state[5]:.2f} rad\n"
            f"Angle of the left leg joint: {state[6]:.2f} rad\n"
            f"Angle of the left foot joint: {state[7]:.2f} rad\n"
            f"Velocity of the x-coordinate of the top: {state[8]:.2f} m/s\n"
            f"Velocity of the z-coordinate (height) of the top: {state[9]:.2f} m/s\n"
            f"Angular velocity of the angle of the top: {state[10]:.2f} rad/s\n"
            f"Angular velocity of the thigh hinge: {state[11]:.2f} rad/s\n"
            f"Angular velocity of the leg hinge: {state[12]:.2f} rad/s\n"
            f"Angular velocity of the foot hinge: {state[13]:.2f} rad/s\n"
            f"Angular velocity of the thigh hinge (left): {state[14]:.2f} rad/s\n"
            f"Angular velocity of the leg hinge (left): {state[15]:.2f} rad/s\n"
            f"Angular velocity of the foot hinge (left): {state[16]:.2f} rad/s"
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
            "The goal in the Walker2D environment is to coordinate both sets of feet, legs, and thighs "
            "to move in the forward (right) direction by applying torques to the six hinges connecting "
            "the six body parts. The objective is to make the robot walk forward."
        )

    def describe_game(self):
        return (
            "In the Walker2D environment, you control a two-dimensional two-legged walker with four main body parts. "
            "Your objective is to make the walker move forward by coordinating the torques applied to the six hinges "
            "connecting the body parts. The environment provides observations of the walker's body parts and velocities, "
            "including the torso, leg, and thigh angles, orientations, and velocities. The goal is to make the walker walk "
            "forward in the positive x-direction."
        )

    def describe_action(self):
        return (
            "Your next move: \nPlease provide a list of six numerical values, each within the range of [-1, 1], "
            "representing the torques to be applied at the six hinge joints of the walker. These torques will help "
            "coordinate the walker's movements and make it walk in the desired direction."
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
            action_desc = (
                "Torques Applied: "
                f"Thigh: {info['action'][0]:.2f}, Leg: {info['action'][1]:.2f}, Foot: {info['action'][2]:.2f}, "
                f"Left Thigh: {info['action'][3]:.2f}, Left Leg: {info['action'][4]:.2f}, Left Foot: {info['action'][5]:.2f}"
            )
            reward_desc = f"Result: Reward of {info['reward']:.2f}"
            next_state_desc = BasicLevelTranslator().translate(info['next_state'])
            descriptions.append(
                f"{state_desc}\n{action_desc}\n{reward_desc}\nTransit to\n{next_state_desc}"
            )
        return descriptions
