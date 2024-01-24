'''Reacher
Action Space Box(-1.0, 1.0, (2,), float32)

Observation Space Box(-inf, inf, (11,), float64)
'''
class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        (cos_angle_arm1, cos_angle_arm2, sin_angle_arm1, sin_angle_arm2, 
         target_x, target_y, angular_vel_arm1, angular_vel_arm2, 
         diff_x, diff_y, diff_z) = state

        res = (f"Arm1 has a cosine angle of {cos_angle_arm1:.2f} and a sine angle of {sin_angle_arm1:.2f}. "\
               f"Arm2 has a cosine angle of {cos_angle_arm2:.2f} and a sine angle of {sin_angle_arm2:.2f}. "\
               f"Target position is at ({target_x:.2f}, {target_y:.2f}). "\
               f"Arm1's angular velocity is {angular_vel_arm1:.2f} rad/s, and Arm2's is {angular_vel_arm2:.2f} rad/s. "\
               f"Vector difference between fingertip and target is ({diff_x:.2f}, {diff_y:.2f}, {diff_z:.2f}).")
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
        return "The goal is to control a two-jointed robot arm to move its end effector (fingertip) close to a randomly spawned target."

    def describe_game(self):
        return ("In the Reacher game, you control a two-jointed robot arm. The objective is to maneuver the arm's fingertip close to a target. "\
                "The observation space includes the cosine and sine of the arm angles, coordinates of the target, angular velocities of the arms, "\
                "and the vector from the fingertip to the target. The episode ends after 50 timesteps or if any state space value becomes non-finite. "\
                "Rewards are given based on the distance of the fingertip from the target and the magnitude of actions applied.")

    def describe_action(self):
        return ("Your next move: \n Please provide two numerical values representing the torques applied at the two hinge joints. "\
                "Each value should be within the range of [-1, 1].")

class TransitionTranslator(ObsTranslator):
    def translate(self, infos, is_current=False):
        descriptions = []
        if is_current:
            state_desc = ObsTranslator().translate(infos[-1]['state'])
            return state_desc
        for i, info in enumerate(infos):
            assert 'state' in info, "info should contain state information"

            state_desc = ObsTranslator().translate(info['state'])
            action_desc = ("Take Action: Apply Torque at Joint 1: {:.2f}, "
                           "Joint 2 Torque: {:.2f}"
                          ).format(info['action'][0], info['action'][1])

            reward_desc = f"Result: Reward of {info['reward']:.2f}, "
            next_state_desc = ObsTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\\n {action_desc} \\n {reward_desc} \\n Transit to {next_state_desc}")
        return descriptions
