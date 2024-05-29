# [Translator classes and functions for Atari QBert environment]

class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        player_x, player_y, player_column, red_enemy_column, green_enemy_column, score_0, score_1, score_2, \
        tile_color_0, tile_color_1, tile_color_2, tile_color_3, tile_color_4, tile_color_5, tile_color_6, tile_color_7, \
        tile_color_8, tile_color_9, tile_color_10, tile_color_11, tile_color_12, tile_color_13, tile_color_14, tile_color_15, \
        tile_color_16, tile_color_17, tile_color_18, tile_color_19, tile_color_20 = state

        player_score = score_0 * 10000 + score_1 * 100 + score_2
        tile_colors = [
            tile_color_0, tile_color_1, tile_color_2, tile_color_3, tile_color_4, tile_color_5,
            tile_color_6, tile_color_7, tile_color_8, tile_color_9, tile_color_10, tile_color_11,
            tile_color_12, tile_color_13, tile_color_14, tile_color_15, tile_color_16, tile_color_17,
            tile_color_18, tile_color_19, tile_color_20
        ]

        return f"You are at position ({player_x}, {player_y}) in column {player_column}. " \
               f"Red enemy is in column {red_enemy_column}. " \
               f"Green enemy is in column {green_enemy_column}. " \
               f"Player's score: {player_score}. " \
               f"Tile colors: {tile_colors}."


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
        return "The goal is to change the color of every tile on the pyramid by hopping on them while avoiding enemies."

    def translate_terminate_state(self, state, episode_len, max_episode_len):
        player_score = state[5] * 10000 + state[6] * 100 + state[7]
        return f"Game over. Final score: {player_score}."

    def translate_potential_next_state(self, state, action):
        return f"After taking the action, you might move to position ({state[0]}, {state[1]}) in column {state[2]} " \
               f"with the red enemy in column {state[3]} and the green enemy in column {state[4]}."

    def describe_game(self):
        return "In the QBert game, you control a character and aim to change the color of every tile on the pyramid by hopping on them while avoiding enemies. " \
               f"There are {self.args.frameskip} frames per step and the action sticks for the skipping frames." if self.args.frameskip > 0 else "" \
               "Scoring Points: Points are scored by changing the color of tiles and defeating enemies. " \
               "You can control the movement of your character to navigate the pyramid, change tile colors, and avoid or defeat enemies."

    def describe_action(self):
        return "Type 1 for NOOP (no operation), 2 to FIRE (trigger fire button), 3 to move UP, 4 to move RIGHT, 5 to move LEFT, 6 to move DOWN. " \
               "Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6]."


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
        else:
            return "Take Action: 'Invalid action'"