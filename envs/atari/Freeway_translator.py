# [Translator classes and functions for Atari Freeway environment]

class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        player_y, score, enemy_car_x_0, enemy_car_x_1, enemy_car_x_2, enemy_car_x_3, enemy_car_x_4, enemy_car_x_5, enemy_car_x_6, enemy_car_x_7, enemy_car_x_8, enemy_car_x_9 = state

        enemy_car_positions = [
            enemy_car_x_0, enemy_car_x_1, enemy_car_x_2, enemy_car_x_3, enemy_car_x_4, 
            enemy_car_x_5, enemy_car_x_6, enemy_car_x_7, enemy_car_x_8, enemy_car_x_9
        ]

        return f"The You are at position y={player_y}. " \
               f"Your score is {score}. " \
               f"Enemy cars are at positions {enemy_car_positions}."


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
        return "The goal is to move the player across the road while avoiding cars to score points."

    def translate_terminate_state(self, state, episode_len, max_episode_len):
        return f"Game over. Final score: {state[1]}."

    def translate_potential_next_state(self, state, action):
        return f"After taking the action, you might move to position y={state[0]} and encounter enemy cars at positions {state[2:]}."

    def describe_game(self):
        return "In the Freeway game, you control a player character and aim to cross a busy road while avoiding cars. " \
               f"There are {self.args.frameskip} frames per step and the action sticks for the skipping frames." if self.args.frameskip > 0 else "" \
               "Scoring Points: Points are scored by successfully crossing the road. " \
               "You can control the movement of your character to dodge cars and reach the other side. Cross as many times as possible to achieve a high score!"

    def describe_action(self):
        return "Type 1 for NOOP (no operation), 2 to move UP, 3 to move DOWN. " \
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
            return "Take Action: 'Move UP'"
        elif action == 3:
            return "Take Action: 'Move DOWN'"
        else:
            return "Take Action: 'Invalid action'"