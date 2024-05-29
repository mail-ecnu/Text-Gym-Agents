# [Translator classes and functions for Atari Space Invaders environment]

class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        invaders_left_count, player_score, num_lives, player_x, enemies_x, missiles_y, enemies_y = state
        # breakpoint()
        enemies_positions = [enemies_x, enemies_y]
        missiles_positions = [missiles_y]

        return f"You are at position x={player_x}. " \
               f"Number of invaders left: {invaders_left_count}. " \
               f"Player's score: {player_score}. " \
               f"Number of lives left: {num_lives}. " \
               f"Enemies are at positions: {enemies_positions}. " \
               f"Missiles are at y positions: {missiles_positions}."


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
        return "The goal is to destroy all the invaders while avoiding their attacks and protecting your lives."

    def translate_terminate_state(self, state, episode_len, max_episode_len):
        return f"Game over. Final score: {state[1]}."

    def translate_potential_next_state(self, state, action):
        enemies_positions = [state[4], state[6]]
        missiles_positions = [state[5]]
        return f"After taking the action, you might move to position x={state[3]} with the enemies at positions {enemies_positions} and missiles at y positions {missiles_positions}."

    def describe_game(self):
        return "In the Space Invaders game, you control a spaceship and aim to destroy all the invaders while avoiding their attacks and protecting your lives. " \
               f"There are {self.args.frameskip} frames per step and the action sticks for the skipping frames." if self.args.frameskip > 0 else "" \
               "Scoring Points: Points are scored by destroying invaders. " \
               "You can control the movement and actions of your spaceship to dodge attacks and shoot at invaders to achieve a high score."

    def describe_action(self):
        return "Type 1 for NOOP (no operation), 2 to FIRE (trigger fire button), 3 to move RIGHT, 4 to move LEFT, 5 to move RIGHT and FIRE, 6 to move LEFT and FIRE. " \
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
            return "Take Action: 'Move RIGHT'"
        elif action == 4:
            return "Take Action: 'Move LEFT'"
        elif action == 5:
            return "Take Action: 'Move RIGHT and FIRE'"
        elif action == 6:
            return "Take Action: 'Move LEFT and FIRE'"
        else:
            return "Take Action: 'Invalid action'"