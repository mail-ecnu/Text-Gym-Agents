class BasicLevelTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        (
            torso_z_coordinate,
            torso_x_orientation,
            torso_y_orientation,
            torso_z_orientation,
            torso_w_orientation,
            front_left_hip_angle,
            front_left_link_angle,
            front_right_hip_angle,
            front_right_link_angle,
            back_left_hip_angle,
            back_left_link_angle,
            back_right_hip_angle,
            back_right_link_angle,
            torso_x_velocity,
            torso_y_velocity,
            torso_z_velocity,
            torso_x_angular_velocity,
            torso_y_angular_velocity,
            torso_z_angular_velocity,
            front_left_hip_angular_velocity,
            front_left_link_angular_velocity,
            front_right_hip_angular_velocity,
            front_right_link_angular_velocity,
            back_left_hip_angular_velocity,
            back_left_link_angular_velocity,
            back_right_hip_angular_velocity,
            back_right_link_angular_velocity,
        ) = state[:27]

        res = (
            f"Torso Z-coordinate: {torso_z_coordinate:.2f}, "
            f"Torso X-orientation: {torso_x_orientation:.2f}, "
            f"Torso Y-orientation: {torso_y_orientation:.2f}, "
            f"Torso Z-orientation: {torso_z_orientation:.2f}, "
            f"Torso W-orientation: {torso_w_orientation:.2f}, "
            f"Front Left Hip Angle: {front_left_hip_angle:.2f}, "
            f"Front Left Link Angle: {front_left_link_angle:.2f}, "
            f"Front Right Hip Angle: {front_right_hip_angle:.2f}, "
            f"Front Right Link Angle: {front_right_link_angle:.2f}, "
            f"Back Left Hip Angle: {back_left_hip_angle:.2f}, "
            f"Back Left Link Angle: {back_left_link_angle:.2f}, "
            f"Back Right Hip Angle: {back_right_hip_angle:.2f}, "
            f"Back Right Link Angle: {back_right_link_angle:.2f}, "
            f"Torso X Velocity: {torso_x_velocity:.2f}, "
            f"Torso Y Velocity: {torso_y_velocity:.2f}, "
            f"Torso Z Velocity: {torso_z_velocity:.2f}, "
            f"Torso X Angular Velocity: {torso_x_angular_velocity:.2f}, "
            f"Torso Y Angular Velocity: {torso_y_angular_velocity:.2f}, "
            f"Torso Z Angular Velocity: {torso_z_angular_velocity:.2f}, "
            f"Front Left Hip Angular Velocity: {front_left_hip_angular_velocity:.2f}, "
            f"Front Left Link Angular Velocity: {front_left_link_angular_velocity:.2f}, "
            f"Front Right Hip Angular Velocity: {front_right_hip_angular_velocity:.2f}, "
            f"Front Right Link Angular Velocity: {front_right_link_angular_velocity:.2f}, "
            f"Back Left Hip Angular Velocity: {back_left_hip_angular_velocity:.2f}, "
            f"Back Left Link Angular Velocity: {back_left_link_angular_velocity:.2f}, "
            f"Back Right Hip Angular Velocity: {back_right_hip_angular_velocity:.2f}, "
            f"Back Right Link Angular Velocity: {back_right_link_angular_velocity:.2f}"
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
        return "The goal is to coordinate the four legs of the ant robot to move forward."

    def describe_game(self):
        return (
            "In the Ant environment, you control a 3D robot called the ant. The ant has a torso with four legs, "
            "each consisting of two links and connected by hinge joints. Your objective is to apply torques to "
            "the eight hinge joints to coordinate the four legs and make the ant move forward in the positive x-direction. "
            "The environment provides observations of the ant's body parts and velocities, including the torso and leg angles, "
            "orientations, and velocities. The episode ends when the ant becomes unhealthy, which can be due to various conditions."
        )

    def describe_action(self):
        return (
            "Your next move: \n Please choose your action which applies torques at the eight hinge joints of the ant. It be a list of eight numerical values and  each value is within the range of [-1,1]."
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
                "Take Action: "
                "Apply Front Left Hip Torque: {:.2f}, "
                "Apply Front Left Link Torque: {:.2f}, "
                "Apply Front Right Hip Torque: {:.2f}, "
                "Apply Front Right Link Torque: {:.2f}, "
                "Apply Back Left Hip Torque: {:.2f}, "
                "Apply Back Left Link Torque: {:.2f}, "
                "Apply Back Right Hip Torque: {:.2f}, "
                "Apply Back Right Link Torque: {:.2f}"
            ).format(
                info['action'][0], info['action'][1], info['action'][2], info['action'][3],
                info['action'][4], info['action'][5], info['action'][6], info['action'][7]
            )

            reward_desc = f"Result: Reward of {info['reward']:.2f}, "
            next_state_desc = BasicLevelTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\\n {action_desc} \\n {reward_desc} \\n Transit to {next_state_desc}")
        return descriptions