# [Translator classes and functions for Atari Boxing environment]
#'labels': {'player_y': 109, 'player_x': 188, 'enemy_y': 20, 'enemy_x': 64, 'ball_x': 0, 'ball_y': 0, 'enemy_score': 0, 'player_score': 0}
class BasicLevelTranslator:
    def __init__(self, ):
        pass

    def translate(self, state):
        player_y, player_x, enemy_y, enemy_x, ball_x, ball_y, enemy_score, player_score = state
        return f"The player is at position ({player_y, player_x}, your opponent is at position ({enemy_y, enemy_x}) ), the ball is at ({ball_y, ball_x})" \
               f"your oppoent's score is {enemy_score}, your score is {player_score}."


class GameDescriber:
    def __init__(self, args):
        self.is_only_local_obs = args.is_only_local_obs == 1
        self.max_episode_len = args.max_episode_len
        self.action_desc_dict = {
        }
        self.reward_desc_dict = {
        }

    def describe_goal(self):
        return "The goal is to knock out your opponent."

    def translate_terminate_state(self, state, episode_len, max_episode_len):
        return ""

    def translate_potential_next_state(self, state, action):
        return ""

    def describe_game(self):
        return "In the Pong game, you play the ball with your opponent, each player rallys the ball by moving the paddles on the playfield. " \
               "Paddles move only vertically on the playfield. A player scores one point when the opponent hits the ball out of bounds or misses a hit. " \
               "The first player to score 21 points wins the game."

    def describe_action(self):
        return "Type '1' for NOOP (no operation), '2' to hit the ball, " \
               "'3' to move right, '4' to move left, '5' to move right while hit the ball, '6' to move left while hit the ball. Ensure you only provide the action number " \
               "from the valid action list, i.e., [1, 2, 3, 4, 5, 6]."


class BasicStateSequenceTranslator(BasicLevelTranslator):
    def translate(self, infos, is_current=False):
        descriptions = []
        if is_current:
            state_desc = BasicLevelTranslator().translate(infos[-1]['state'])
            return state_desc
        for i, info in enumerate(infos):
            assert 'state' in info, "info should contain state information"

            state_desc = BasicLevelTranslator().translate(info['state'])
            if info['action'] == 1:
                action_desc = f"Take Action: 'Do nothing'"
            elif info['action'] == 2:
                action_desc = f"Take Action: 'Hit your ball'"
            elif info['action'] == 3:
                action_desc = f"Take Action: 'Move right'"
            elif info['action'] == 4:
                action_desc = f"Take Action: 'Move left'"
            elif info['action'] == 5:
                action_desc = f"Take Action: 'Move right while hiting the ball'"
            else:
                action_desc = f"Take Action: 'Move left while hiting the ball'"
            reward_desc = f"Result: Reward of {info['reward']}, "
            next_state_desc = BasicLevelTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\n {action_desc} \n {reward_desc} \n Transit to {next_state_desc}")
        return descriptions
