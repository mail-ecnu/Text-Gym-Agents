# [Translator classes and functions for Atari Demon Attack environment]

class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        level, player_x, enemy_x1, enemy_x2, enemy_x3, missile_y, enemy_y1, enemy_y2, enemy_y3, num_lives = state

        enemy_positions = [(enemy_x1, enemy_y1), (enemy_x2, enemy_y2), (enemy_x3, enemy_y3)]

        return f"You are at position x={player_x}. " \
               f"Missile is at position y={missile_y}. " \
               f"Enemy positions are {enemy_positions}. " \
               f"You are on level {level}. " \
               f"You have {num_lives} lives remaining."


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
        return "The goal is to destroy all the enemies while avoiding their attacks to progress through levels."

    def translate_terminate_state(self, state, episode_len, max_episode_len):
        return f"Game over. You reached level {state[0]}."

    def translate_potential_next_state(self, state, action):
        return f"After taking the action, you might move to position x={state[1]} and interact with enemies at positions {[(state[2], state[6]), (state[3], state[7]), (state[4], state[8])]}."

    def describe_game(self):
        return "In the Demon Attack game, you control a player character and aim to destroy enemy demons while avoiding their attacks. " \
               f"There are {self.args.frameskip} frames per step and the action sticks for the skipping frames." if self.args.frameskip > 0 else "" \
               "Scoring Points: Points are scored by destroying enemy demons. " \
               "You can control the movement and firing of your character to dodge attacks and hit enemies. Destroy all enemies to progress through levels!"

    def describe_action(self):
        return "Type 1 for NOOP (no operation), 2 to FIRE, 3 to move RIGHT, 4 to move LEFT, " \
               "5 to RIGHT FIRE, 6 to LEFT FIRE. " \
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
            return "Take Action: 'RIGHT FIRE'"
        elif action == 6:
            return "Take Action: 'LEFT FIRE'"
        else:
            return "Take Action: 'Invalid action'"