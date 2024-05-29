# [Translator classes and functions for Atari Breakout environment]

class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        ball_x, ball_y, player_x, blocks_hit_count, score, \
        block_bit_map_0, block_bit_map_1, block_bit_map_2, block_bit_map_3, block_bit_map_4, block_bit_map_5, \
        block_bit_map_6, block_bit_map_7, block_bit_map_8, block_bit_map_9, block_bit_map_10, block_bit_map_11, \
        block_bit_map_12, block_bit_map_13, block_bit_map_14, block_bit_map_15, block_bit_map_16, block_bit_map_17, \
        block_bit_map_18, block_bit_map_19, block_bit_map_20, block_bit_map_21, block_bit_map_22, block_bit_map_23, \
        block_bit_map_24, block_bit_map_25, block_bit_map_26, block_bit_map_27, block_bit_map_28, block_bit_map_29 = state

        block_bit_map = [
            block_bit_map_0, block_bit_map_1, block_bit_map_2, block_bit_map_3, block_bit_map_4, block_bit_map_5,
            block_bit_map_6, block_bit_map_7, block_bit_map_8, block_bit_map_9, block_bit_map_10, block_bit_map_11,
            block_bit_map_12, block_bit_map_13, block_bit_map_14, block_bit_map_15, block_bit_map_16, block_bit_map_17,
            block_bit_map_18, block_bit_map_19, block_bit_map_20, block_bit_map_21, block_bit_map_22, block_bit_map_23,
            block_bit_map_24, block_bit_map_25, block_bit_map_26, block_bit_map_27, block_bit_map_28, block_bit_map_29
        ]

        return f"The ball is at position ({ball_x}, {ball_y}). " \
               f"The player paddle is at position x={player_x}. " \
               f"Blocks hit count is {blocks_hit_count}. " \
               f"Your score is {score}. " \
               f"Block bit map: {block_bit_map}."


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
        return "The goal is to destroy all the blocks by hitting them with the ball while keeping the ball in play using the paddle."

    def translate_terminate_state(self, state, episode_len, max_episode_len):
        return f"Game over. Final score: {state[4]}."

    def translate_potential_next_state(self, state, action):
        return f"After taking the action, you might move the paddle to x={state[2]} and the ball might be at ({state[0]}, {state[1]})."

    def describe_game(self):
        return "In the Breakout game, you control a paddle and aim to destroy blocks by hitting them with a ball. " \
               f"There are {self.args.frameskip} frames per step and the action sticks for the skipping frames." if self.args.frameskip > 0 else "" \
               "Scoring Points: Points are scored by hitting and destroying blocks with the ball. " \
               "You can control the movement of the paddle to keep the ball in play and direct it towards the blocks. Destroy all blocks to win!"

    def describe_action(self):
        return "Type 1 for NOOP (no operation), 2 to FIRE, 3 to move RIGHT, 4 to move LEFT. " \
               "Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4]."


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
            return "Take Action: 'Move RIGHT'"
        elif action == 4:
            return "Take Action: 'Move LEFT'"
        else:
            return "Take Action: 'Invalid action'"