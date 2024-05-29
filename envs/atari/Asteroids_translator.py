# [Translator classes and functions for Atari Asteroids environment]

class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        player_x, player_y, num_lives_direction, player_score_high, player_score_low, \
        player_missile_x1, player_missile_x2, player_missile_y1, player_missile_y2, \
        player_missile1_direction, player_missile2_direction, \
        enemy_asteroids_y_0, enemy_asteroids_y_1, enemy_asteroids_y_2, enemy_asteroids_y_3, \
        enemy_asteroids_y_4, enemy_asteroids_y_5, enemy_asteroids_y_6, enemy_asteroids_y_7, \
        enemy_asteroids_y_8, enemy_asteroids_y_9, enemy_asteroids_y_10, enemy_asteroids_y_11, \
        enemy_asteroids_y_12, enemy_asteroids_y_13, enemy_asteroids_y_14, \
        enemy_asteroids_x_0, enemy_asteroids_x_1, enemy_asteroids_x_2, enemy_asteroids_x_3, \
        enemy_asteroids_x_4, enemy_asteroids_x_5, enemy_asteroids_x_6, enemy_asteroids_x_7, \
        enemy_asteroids_x_8, enemy_asteroids_x_9, enemy_asteroids_x_10, enemy_asteroids_x_11, \
        enemy_asteroids_x_12, enemy_asteroids_x_13, enemy_asteroids_x_14 = state

        player_score = player_score_high * 256 + player_score_low
        asteroids_positions = [(enemy_asteroids_x_0, enemy_asteroids_y_0), (enemy_asteroids_x_1, enemy_asteroids_y_1),
                               (enemy_asteroids_x_2, enemy_asteroids_y_2), (enemy_asteroids_x_3, enemy_asteroids_y_3),
                               (enemy_asteroids_x_4, enemy_asteroids_y_4), (enemy_asteroids_x_5, enemy_asteroids_y_5),
                               (enemy_asteroids_x_6, enemy_asteroids_y_6), (enemy_asteroids_x_7, enemy_asteroids_y_7),
                               (enemy_asteroids_x_8, enemy_asteroids_y_8), (enemy_asteroids_x_9, enemy_asteroids_y_9),
                               (enemy_asteroids_x_10, enemy_asteroids_y_10), (enemy_asteroids_x_11, enemy_asteroids_y_11),
                               (enemy_asteroids_x_12, enemy_asteroids_y_12), (enemy_asteroids_x_13, enemy_asteroids_y_13),
                               (enemy_asteroids_x_14, enemy_asteroids_y_14)]
        missiles_positions = [(player_missile_x1, player_missile_y1), (player_missile_x2, player_missile_y2)]

        return f"You are at position ({player_x}, {player_y}), with {num_lives_direction} lives left. " \
               f"Your score is {player_score}. " \
               f"Missiles are at positions {missiles_positions}. " \
               f"Asteroids are at positions {asteroids_positions}."


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
        return "The goal is to destroy as many asteroids as possible without getting hit."

    def translate_terminate_state(self, state, episode_len, max_episode_len):
        return f"Game over. Final score: {state[3] * 256 + state[4]}."

    def translate_potential_next_state(self, state, action):
        return f"After taking the action, you might move to position ({state[0]}, {state[1]}) and interact with asteroids at positions {[(state[15 + i], state[26 + i]) for i in range(15)]}."

    def describe_game(self):
        return "In the Asteroids game, you control a spaceship and aim to destroy asteroids while avoiding collisions. " \
               f"There are {self.args.frameskip} frames per step and the action sticks for the skipping frames." if self.args.frameskip > 0 else "" \
               "Scoring Points: Points are scored by destroying asteroids. " \
               "You can control the movement and firing of your spaceship. Avoid getting hit by asteroids to survive!"

    def describe_action(self):
        return "Type 1 for NOOP (no operation), 2 to FIRE, 3 to move UP, 4 to move RIGHT, 5 to move LEFT, " \
               "6 to move DOWN, 7 to move UPRIGHT, 8 to move UPLEFT, 9 to move UP and FIRE, 10 to move RIGHT and FIRE, " \
               "11 to move LEFT and FIRE, 12 to move DOWN and FIRE, 13 to move UPRIGHT and FIRE, 14 to move UPLEFT and FIRE. " \
               "Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]."


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
            return "Take Action: 'Move UP and FIRE'"
        elif action == 10:
            return "Take Action: 'Move RIGHT and FIRE'"
        elif action == 11:
            return "Take Action: 'Move LEFT and FIRE'"
        elif action == 12:
            return "Take Action: 'Move DOWN and FIRE'"
        elif action == 13:
            return "Take Action: 'Move UPRIGHT and FIRE'"
        elif action == 14:
            return "Take Action: 'Move UPLEFT and FIRE'"
        else:
            return "Take Action: 'Invalid action'"