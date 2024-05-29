# [Translator classes and functions for Atari Video Pinball environment]

class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        ball_x, ball_y, player_left_paddle_y, player_right_paddle_y, score_1, score_2 = state

        player_score = score_1 * 100 + score_2

        return f"Ball is at position ({ball_x}, {ball_y}). " \
               f"Left paddle is at position y={player_left_paddle_y}. " \
               f"Right paddle is at position y={player_right_paddle_y}. " \
               f"Player's score: {player_score}."


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
        return "The goal is to keep the ball in play and score as many points as possible by hitting targets with the ball."

    def translate_terminate_state(self, state, episode_len, max_episode_len):
        player_score = state[4] * 100 + state[5]
        return f"Game over. Final score: {player_score}."

    def translate_potential_next_state(self, state, action):
        return f"After taking the action, the ball might be at position ({state[0]}, {state[1]}) with the left paddle at position y={state[2]} and the right paddle at position y={state[3]}."

    def describe_game(self):
        return "In the Video Pinball game, you control the paddles and aim to keep the ball in play and score as many points as possible by hitting targets with the ball. " \
               f"There are {self.args.frameskip} frames per step and the action sticks for the skipping frames." if self.args.frameskip > 0 else "" \
               "Scoring Points: Points are scored by hitting targets with the ball. " \
               "You can control the movement of the paddles to keep the ball in play and aim at targets to achieve a high score."

    def describe_action(self):
        return "Type 1 for NOOP (no operation), 2 to FIRE (trigger fire button), 3 to move UP, 4 to move RIGHT, 5 to move LEFT, 6 to move DOWN, " \
               "7 to move UP and FIRE, 8 to move RIGHT and FIRE, 9 to move LEFT and FIRE. " \
               "Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6, 7, 8, 9]."


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
            return "Take Action: 'Move UP and FIRE'"
        elif action == 8:
            return "Take Action: 'Move RIGHT and FIRE'"
        elif action == 9:
            return "Take Action: 'Move LEFT and FIRE'"
        else:
            return "Take Action: 'Invalid action'"