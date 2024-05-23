# [Translator classes and functions for Atari Skiing environment]

class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        player_x, clock_m, clock_s, clock_ms, score, \
        object_y_0, object_y_1, object_y_2, object_y_3, object_y_4, object_y_5, object_y_6 = state

        clock_time = f"{clock_m:02}:{clock_s:02}.{clock_ms:03}"
        object_positions = [object_y_0, object_y_1, object_y_2, object_y_3, object_y_4, object_y_5, object_y_6]

        return f"You are at position x={player_x}. " \
               f"The current time is {clock_time}. " \
               f"Your score is {score}. " \
               f"Objects are at positions {object_positions}."


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
        return "The goal is to ski down the slope and avoid obstacles to achieve the best time and score."

    def translate_terminate_state(self, state, episode_len, max_episode_len):
        return f"Game over. Final score: {state[4]}."

    def translate_potential_next_state(self, state, action):
        return f"After taking the action, you might move to a new position with the player at x={state[0]} and objects at positions {state[5:]}."

    def describe_game(self):
        return "In the Skiing game, you control a skier and aim to navigate down the slope while avoiding obstacles. " \
               f"There are {self.args.frameskip} frames per step and the action sticks for the skipping frames." if self.args.frameskip > 0 else "" \
               "Scoring Points: Points are scored based on time and avoiding obstacles. " \
               "You can control the direction of your skier to maneuver through the course. Avoid hitting obstacles to maintain your speed and score!"

    def describe_action(self):
        return "Type '1' for NOOP (no operation), '2' to move RIGHT, '3' to move LEFT. " \
               "Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3]."


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
            return "Take Action: 'Move RIGHT'"
        elif action == 3:
            return "Take Action: 'Move LEFT'"
        else:
            return "Take Action: 'Invalid action'"