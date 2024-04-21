class BasicLevelTranslator:
    def __init__(self):
        pass
    
    def translate(self, state):
        (front_tip_z, front_tip_angle, back_thigh_angle_1, back_shin_angle_1, 
         tip_velocity_x, tip_velocity_y, front_tip_angular_velocity, 
         back_thigh_angular_velocity_1, front_tip_x, front_tip_y, front_tip_angle_2, 
         back_thigh_angle_2, back_shin_angle_2, tip_velocity_angular_x, 
         tip_velocity_angular_y, front_tip_angular_velocity_2, 
         back_thigh_angular_velocity_2) = state[:17]

        res = (
            f"The front tip is at a z-coordinate of {front_tip_z:.2f} meters. "
            f"The angle of the front tip is {front_tip_angle:.2f} radians. "
            f"The angles of the back thigh are {back_thigh_angle_1:.2f} and {back_thigh_angle_2:.2f} radians. "
            f"The angles of the back shin are {back_shin_angle_1:.2f} and {back_shin_angle_2:.2f} radians. "
            f"The tip has velocity along the x-axis of {tip_velocity_x:.2f} m/s. "
            f"The tip has velocity along the y-axis of {tip_velocity_y:.2f} m/s. "
            f"The angular velocity of the front tip is {front_tip_angular_velocity:.2f} radians/s. "
            f"The angular velocities of the back thigh are {back_thigh_angular_velocity_1:.2f} and {back_thigh_angular_velocity_2:.2f} radians/s. "
            f"The x-coordinate of the front tip is {front_tip_x:.2f} meters. "
            f"The y-coordinate of the front tip is {front_tip_y:.2f} meters. "
            f"The angle of the front tip is {front_tip_angle_2:.2f} radians. "
            f"The angular velocity of the tip along the x-axis is {tip_velocity_angular_x:.2f} radians/s. "
            f"The angular velocity of the tip along the y-axis is {tip_velocity_angular_y:.2f} radians/s. "
            f"The angular velocity of the back shin is {front_tip_angular_velocity_2:.2f} radians/s."
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
        return "The goal is to make the Half-Cheetah run forward (right) as fast as possible."

    def describe_game(self):
        return (
            "In the Half-Cheetah game, you control a 2-dimensional robot with 9 links and 8 joints. "
            "The goal is to apply torque to the joints to make the cheetah run forward (right) as fast as possible. "
            "You can control the back thigh, back shin, and back foot rotors for the back legs, and the front thigh, "
            "front shin, and front foot rotors for the front legs. The episode ends after 1000 timesteps. "
            "Your reward is based on how much forward progress you make and how much control effort you apply."
        )

    def describe_action(self):
        return ("Type six numerical values, each one within the range of [-1,1], "
            "which represents the torque being applied to the back thigh rotor, "
            "back shin rotor, back foot rotor, front thigh rotor, front shin rotor, "
            "and front foot rotor respectively."
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
                "Apply Back Thigh Torque: {:.2f}, "
                "Apply Back Shin Torque: {:.2f}, "
                "Apply Back Foot Torque: {:.2f}, "
                "Apply Front Thigh Torque: {:.2f}, "
                "Apply Front Shin Torque: {:.2f}, "
                "Apply Front Foot Torque: {:.2f}"
            ).format(
                info['action'][0], info['action'][1], info['action'][2],
                info['action'][3], info['action'][4], info['action'][5]
            )

            reward_desc = f"Result: Forward Reward of {info['forward_reward']:.2f}, "
            ctrl_cost_desc = f"Control Cost of {info['ctrl_cost']:.2f}, "
            total_reward_desc = f"Total Reward of {info['reward']:.2f}, "
            next_state_desc = BasicLevelTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\\n {action_desc} \\n {reward_desc} {ctrl_cost_desc} {total_reward_desc} \\n Transit to {next_state_desc}")
        return descriptions
