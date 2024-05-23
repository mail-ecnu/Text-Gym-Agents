# [Translator classes and functions for Atari BattleZone environment]

class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        blue_tank_facing_direction, blue_tank_size_y, blue_tank_x, blue_tank2_facing_direction, blue_tank2_size_y, blue_tank2_x, \
        num_lives, missile_y, compass_needles_angle, angle_of_tank, left_tread_position, right_tread_position, crosshairs_color, score = state

        return f"The blue tank is facing direction {blue_tank_facing_direction} and is at position x={blue_tank_x} with size y={blue_tank_size_y}. " \
               f"The second blue tank is facing direction {blue_tank2_facing_direction} and is at position x={blue_tank2_x} with size y={blue_tank2_size_y}. " \
               f"You have {num_lives} lives remaining. " \
               f"The missile is at position y={missile_y}. " \
               f"The compass needle is at an angle of {compass_needles_angle}. " \
               f"The tank's angle is {angle_of_tank}. " \
               f"The left tread position is {left_tread_position} and the right tread position is {right_tread_position}. " \
               f"The crosshairs color is {crosshairs_color}. " \
               f"Your score is {score}."


class GameDescriber:
    def __init__(self, args):
        self.is_only_local_obs = args.is_only_local_obs == 1
        self.max_episode_len = args.max_episode_len
        self.args = args
        self.action_desc_dict = {
        }
        self.reward_desc_dict = {
        }

    def describe_goal(self):
        return "The goal is to destroy as many enemy tanks as possible and survive as long as you can."

    def translate_terminate_state(self, state, episode_len, max_episode_len):
        return f"Game over. Final score: {state[-1]}."

    def translate_potential_next_state(self, state, action):
        return f"After taking the action, you might move to a new position with the blue tanks at positions {state[2]}, {state[5]} and the missile at position {state[7]}."

    def describe_game(self):
        return "In the BattleZone game, you control a tank and aim to destroy enemy tanks while avoiding being hit. " \
               f"There are {self.args.frameskip} frames per step and the action sticks for the skipping frames." if self.args.frameskip > 0 else "" \
               "Scoring Points: Points are scored by destroying enemy tanks. " \
               "You can control the movement and firing of your tank. Survive as long as possible to achieve a high score!"

    def describe_action(self):
        return "Type '1' for NOOP (no operation), '2' to FIRE, '3' to move UP, '4' to move RIGHT, '5' to move LEFT, '6' to move DOWN, " \
               "'7' to move UPRIGHT, '8' to move UPLEFT, '9' to move DOWNRIGHT, '10' to move DOWNLEFT, '11' to move UP and FIRE, '12' to move RIGHT and FIRE, " \
               "'13' to move LEFT and FIRE, '14' to move DOWN and FIRE, '15' to move UPRIGHT and FIRE, '16' to move UPLEFT and FIRE, '17' to move DOWNRIGHT and FIRE, " \
               "or '18' to move DOWNLEFT and FIRE. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]."


class TransitionTranslator(ObsTranslator):
    def translate(self, infos, is_current=False):
        descriptions = []
        if is_current:
            state_desc = ObsTranslator().translate(infos[-1]['state'])
            return state_desc
        for i, info in enumerate(infos):
            assert 'state' in info, "info should contain state information"

            state_desc = ObsTranslator().translate(info['state'])
            action_desc = self.get_action_description(info['action'])
            reward_desc = f"Result: Reward of {info['reward']}, "
            next_state_desc = ObsTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\n {action_desc} \n {reward_desc} \n Transit to {next_state_desc}")
        return descriptions

    def get_action_description(self, action):
        if action == 1:
            return "Take Action: 'Do nothing (NOOP)'"
        elif action == 2:
            return "Take Action: 'FIRE'"
        elif action == 3:
            return "Take Action: 'Move UP'"
        elif action == 4:
            return "Take Action: 'Move RIGHT'"
        elif action == 5:
            return "Take Action: 'Move LEFT'"
        elif action == 6:
            return "Take Action: 'Move DOWN'"
        elif action == 7:
            return "Take Action: 'Move UPRIGHT'"
        elif action == 8:
            return "Take Action: 'Move UPLEFT'"
        elif action == 9:
            return "Take Action: 'Move DOWNRIGHT'"
        elif action == 10:
            return "Take Action: 'Move DOWNLEFT'"
        elif action == 11:
            return "Take Action: 'Move UP and FIRE'"
        elif action == 12:
            return "Take Action: 'Move RIGHT and FIRE'"
        elif action == 13:
            return "Take Action: 'Move LEFT and FIRE'"
        elif action == 14:
            return "Take Action: 'Move DOWN and FIRE'"
        elif action == 15:
            return "Take Action: 'Move UPRIGHT and FIRE'"
        elif action == 16:
            return "Take Action: 'Move UPLEFT and FIRE'"
        elif action == 17:
            return "Take Action: 'Move DOWNRIGHT and FIRE'"
        elif action == 18:
            return "Take Action: 'Move DOWNLEFT and FIRE'"
        else:
            return "Take Action: 'Invalid action'"