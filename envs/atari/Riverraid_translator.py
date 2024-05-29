# [Translator classes and functions for Atari River Raid environment]

class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        player_x, missile_x, missile_y, fuel_meter_high, fuel_meter_low = state

        fuel_meter = fuel_meter_high * 256 + fuel_meter_low

        return f"You are at position x={player_x}. " \
               f"Missile is at position ({missile_x}, {missile_y}). " \
               f"Fuel meter: {fuel_meter}."


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
        return "The goal is to navigate through the river, avoid obstacles, and destroy enemies while managing your fuel supply."

    def translate_terminate_state(self, state, episode_len, max_episode_len):
        fuel_meter = state[3] * 256 + state[4]
        return f"Game over. Fuel meter: {fuel_meter}."

    def translate_potential_next_state(self, state, action):
        return f"After taking the action, you might move to position x={state[0]} with the missile at position ({state[1]}, {state[2]}) and the fuel meter at {state[3] * 256 + state[4]}."

    def describe_game(self):
        return "In the River Raid game, you control an aircraft and aim to navigate through the river, avoid obstacles, and destroy enemies while managing your fuel supply. " \
               f"There are {self.args.frameskip} frames per step and the action sticks for the skipping frames." if self.args.frameskip > 0 else "" \
               "Scoring Points: Points are scored by destroying enemies and navigating through the river. " \
               "You can control the movement and actions of your aircraft to dodge obstacles, destroy enemies, and manage your fuel supply to achieve a high score."

    def describe_action(self):
        return "Type 1 for NOOP (no operation), 2 to FIRE, 3 to move UP, 4 to move RIGHT, 5 to move LEFT, 6 to move DOWN, " \
               "7 to move UPRIGHT, 8 to move UPLEFT, 9 to move DOWNRIGHT, 10 to move DOWNLEFT, 11 to move UP and FIRE, 12 to move RIGHT and FIRE, " \
               "13 to move LEFT and FIRE, 14 to move DOWN and FIRE, 15 to move UPRIGHT and FIRE, 16 to move UPLEFT and FIRE, 17 to move DOWNRIGHT and FIRE, " \
               "or '18' to move DOWNLEFT and FIRE. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]."


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
            return "Take Action: 'Move DOWNRIGHT'"
        elif action == 10:
            return "Take Action: 'Move DOWNLEFT'"
        elif action == 11:
            return "Take Action: 'Move UP and FIRE'"
        elif action == 12:
            return "Take Action: 'Move RIGHT and FIRE'"
        elif action == 13:
            return "Take Action: 'Move LEFT and FIRE'"
        elif action == 14:
            return "Take Action: 'Move DOWN and FIRE'"
        elif action == 15:
            return "Take Action: 'Move UPRIGHT and FIRE'"
        elif action == 16:
            return "Take Action: 'Move UPLEFT and FIRE'"
        elif action == 17:
            return "Take Action: 'Move DOWNRIGHT and FIRE'"
        elif action == 18:
            return "Take Action: 'Move DOWNLEFT and FIRE'"
        else:
            return "Take Action: 'Invalid action'"