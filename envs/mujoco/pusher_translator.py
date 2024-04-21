'''Pusher
Action Space Box(-2.0, 2.0, (7,), float32)
Observation Space Box(-inf, inf, (23,), float64)
'''
import math

class BasicLevelTranslator:
    def __init__(self):
        pass

    def translate(self, state):

        joint_angles = state[:7]
        joint_velocities = state[7:14]
        fingertip_coords = state[14:17]
        object_coords = state[17:20]
        goal_coords = state[20:]

        joint_angle_degrees = [math.degrees(angle) for angle in joint_angles]
        joint_velocity_degrees = [math.degrees(velocity) for velocity in joint_velocities]

        res = (f"Rotation of the panning shoulder: {joint_angle_degrees[0]:.2f} degrees, "
               f"Rotation of the shoulder lifting joint: {joint_angle_degrees[1]:.2f} degrees, "
               f"Rotation of the shoulder rolling joint: {joint_angle_degrees[2]:.2f} degrees, "
               f"Rotation of the elbow joint: {joint_angle_degrees[3]:.2f} degrees, "
               f"Rotation of the forearm rolling joint: {joint_angle_degrees[4]:.2f} degrees, "
               f"Rotation of the wrist flexing joint: {joint_angle_degrees[5]:.2f} degrees, "
               f"Rotation of the wrist rolling joint: {joint_angle_degrees[6]:.2f} degrees, "
               f"Rotational velocity of the panning shoulder: {joint_velocity_degrees[0]:.2f} degrees/s, "
               f"Rotational velocity of the shoulder lifting joint: {joint_velocity_degrees[1]:.2f} degrees/s, "
               f"Rotational velocity of the shoulder rolling joint: {joint_velocity_degrees[2]:.2f} degrees/s, "
               f"Rotational velocity of the elbow joint: {joint_velocity_degrees[3]:.2f} degrees/s, "
               f"Rotational velocity of the forearm rolling joint: {joint_velocity_degrees[4]:.2f} degrees/s, "
               f"Rotational velocity of the wrist flexing joint: {joint_velocity_degrees[5]:.2f} degrees/s, "
               f"Rotational velocity of the wrist rolling joint: {joint_velocity_degrees[6]:.2f} degrees/s, "
               f"Fingertip coordinates (x, y, z): ({fingertip_coords[0]:.2f}, {fingertip_coords[1]:.2f}, {fingertip_coords[2]:.2f}), "
               f"Object coordinates (x, y, z): ({object_coords[0]:.2f}, {object_coords[1]:.2f}, {object_coords[2]:.2f}), "
               f"Goal coordinates (x, y, z): ({goal_coords[0]:.2f}, {goal_coords[1]:.2f}, {goal_coords[2]:.2f}).")
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
        return "The goal is to move the target cylinder (object) to the goal position using the robot's end effector (fingertip)."

    def describe_game(self):
        return ("In the Pusher game, you control a multi-jointed robot arm to manipulate a target cylinder (object) "
                "and place it in a goal position using the robot's fingertip (end effector). The robot has shoulder, elbow, "
                "forearm, and wrist joints that you can control with torque values. The observation space includes joint angles, "
                "angular velocities of joints, fingertip coordinates, object coordinates, and goal coordinates. The reward is "
                "based on the distance between the fingertip and the object, the distance between the object and the goal, "
                "and control penalties for large actions.")

    def describe_action(self):
        return ("Type 7 numerical values within the range [-2, 2], "
                "representing the torques applied to the robot's joints (shoulder, elbow, forearm, and wrist).")


class BasicStateSequenceTranslator(BasicLevelTranslator):
    def translate(self, infos, is_current=False):
        descriptions = []
        if is_current:
            state_desc = BasicLevelTranslator().translate(infos[-1]['state'])
            return state_desc
        for info in infos:
            assert 'state' in info, "info should contain state information"

            state_desc = BasicLevelTranslator().translate(info['state'])
            action_desc = ("Take Action: Apply Torques - "
                           "Shoulder Pan: {:.2f}, Shoulder Lift: {:.2f}, Shoulder Roll: {:.2f}, "
                           "Elbow Flex: {:.2f}, Forearm Roll: {:.2f}, Wrist Flex: {:.2f}, Wrist Roll: {:.2f}"
                           ).format(info['action'][0], info['action'][1], info['action'][2], info['action'][3],
                                    info['action'][4], info['action'][5], info['action'][6])

            reward_desc = f"Result: Reward of {info['reward']:.2f}"
            next_state_desc = BasicLevelTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}\n{action_desc}\n{reward_desc}\nTransit to {next_state_desc}")
        return descriptions

