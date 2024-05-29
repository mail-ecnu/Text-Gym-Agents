# [Translator classes and functions for Atari Bowling environment]

class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        ball_x, ball_y, player_x, player_y, frame_number_display, score, pin_existence_0, pin_existence_1, pin_existence_2, pin_existence_3, pin_existence_4, pin_existence_5, pin_existence_6, pin_existence_7, pin_existence_8, pin_existence_9 = state
        pins_status = [pin_existence_0, pin_existence_1, pin_existence_2, pin_existence_3, pin_existence_4, pin_existence_5, pin_existence_6, pin_existence_7, pin_existence_8, pin_existence_9]
        pins_down = 10 - sum(pins_status)
        return f"Your ball is at position ({ball_x}, {ball_y}), you are at position ({player_x}, {player_y}), " \
               f"frame number is {frame_number_display}, your score is {score}, " \
               f"{pins_down} pins are down, pins status: {pins_status}."


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
        return "The goal is to knock down as many pins as possible."

    def translate_terminate_state(self, state, episode_len, max_episode_len):
        return f"Game over. Final score: {state[5]}, Pins down: {10 - sum(state[6:])}."

    def translate_potential_next_state(self, state, action):
        return f"After taking the action, you might move to position ({state[2]}, {state[3]}) and the ball to position ({state[0]}, {state[1]})."

    def describe_game(self):
        return "In the Bowling game, you aim to knock down pins by rolling the ball down the lane. " \
               f"There are {self.args.frameskip} frames per step and the action sticks for the skipping frames." if self.args.frameskip > 0 else "" \
               "Scoring Points: Points are scored based on the number of pins knocked down each frame. " \
               "You can control the direction and power of your roll. Aim carefully to knock down all the pins for a strike!"

    def describe_action(self):
        return "Type 1 for NOOP (no operation), 2 to release the ball straight (FIRE), " \
               "3 to move up, 4 to move down, 5 to adjust ball position up and release (UPFIRE), 6 to adjust ball position down and release (DOWNFIRE). " \
               "Ensure you only provide the action number " \
               "from the valid action list, i.e., [1, 2, 3, 4, 5, 6]."


class TransitionTranslator(ObsTranslator):
    def translate(self, infos, is_current=False):
        descriptions = []
        if is_current:
            state_desc = ObsTranslator().translate(infos[-1]['state'])
            return state_desc
        for i, info in enumerate(infos):
            assert 'state' in info, "info should contain state information"

            state_desc = ObsTranslator().translate(info['state'])
            if info['action'] == 1:
                action_desc = f"Take Action: 'Do nothing (NOOP)'"
            elif info['action'] == 2:
                action_desc = f"Take Action: 'Release the ball straight (FIRE)'"
            elif info['action'] == 3:
                action_desc = f"Take Action: 'Move up'"
            elif info['action'] == 4:
                action_desc = f"Take Action: 'Move down'"
            elif info['action'] == 5:
                action_desc = f"Take Action: 'Adjust ball position up and release (UPFIRE)'"
            else:
                action_desc = f"Take Action: 'Adjust ball position down and release (DOWNFIRE)'"
            reward_desc = f"Result: Reward of {info['reward']}, "
            next_state_desc = ObsTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\n {action_desc} \n {reward_desc} \n Transit to {next_state_desc}")
        return descriptions