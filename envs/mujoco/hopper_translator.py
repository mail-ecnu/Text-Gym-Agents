'''
Action Space Box(-1.0, 1.0, (3,), float32)
Observation Space Box(-inf, inf, (11,), float64)
'''

class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        (top_z, top_angle, thigh_angle, leg_angle, foot_angle, 
         top_x_velocity, top_z_velocity, top_angular_velocity, 
         thigh_angular_velocity, leg_angular_velocity, foot_angular_velocity) = state[:11]

        res = (
            f"The top is at a z-coordinate of {top_z:.2f} meters. "
            f"The angle of the top is {top_angle:.2f} radians. "
            f"The angle of the thigh joint is {thigh_angle:.2f} radians. "
            f"The angle of the leg joint is {leg_angle:.2f} radians. "
            f"The angle of the foot joint is {foot_angle:.2f} radians. "
            f"The x-coordinate velocity of the top is {top_x_velocity:.2f} m/s. "
            f"The z-coordinate (height) velocity of the top is {top_z_velocity:.2f} m/s. "
            f"The angular velocity of the top is {top_angular_velocity:.2f} radians/s. "
            f"The angular velocity of the thigh hinge is {thigh_angular_velocity:.2f} radians/s. "
            f"The angular velocity of the leg hinge is {leg_angular_velocity:.2f} radians/s. "
            f"The angular velocity of the foot hinge is {foot_angular_velocity:.2f} radians/s."
        )
        return res

class GameDescriber:
    def __init__(self, args):
        self.is_only_local_obs = args.is_only_local_obs == 1
        self.max_episode_len = args.max_episode_len
        self.action_desc_dict = {}
        self.reward_desc_dict = {}
    
    def translate_terminate_state(self, state, episode_len, max_episode_len):
        return ""
        
    def translate_potential_next_state(self, state, action):
        return ""
    
    def describe_goal(self):
        return (
            "The goal in the Hopper environment is to make the one-legged hopper move forward (right) "
            "by applying torques to the thigh, leg, and foot joints."
        )

    def describe_game(self):
        return (
            "In the Hopper environment, you control a one-legged hopper consisting of a torso, thigh, leg, "
            "and a foot on which it rests. Your objective is to apply torques to the thigh, leg, and foot joints "
            "to make the hopper perform hops in the positive x-direction. The environment provides observations "
            "of the hopper's body parts and velocities, including the height, angles of joints, and angular velocities. "
            "The episode ends when certain termination conditions are met."
        )

    def describe_action(self):
        return (
            "Your next move: \n Please provide a list of three numerical values, each within the range of [-1,1], "
            "representing the torques to be applied at the thigh, leg, and foot joints of the hopper."
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
                f"Take Action: Apply Thigh Torque: {info['action'][0]:.2f}, "
                f"Leg Torque: {info['action'][1]:.2f}, Foot Torque: {info['action'][2]:.2f}"
            )

            reward_desc = f"Result: Reward of {info['reward']:.2f}, "
            next_state_desc = ObsTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\\n {action_desc} \\n {reward_desc} \\n Transit to {next_state_desc}")
        return descriptions

