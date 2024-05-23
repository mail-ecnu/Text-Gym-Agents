# [Translator classes and functions for Atari Boxing environment]

class ObsTranslator:
    def __init__(self,):
        pass

    def translate(self, state):
        player_x, player_y, enemy_x, enemy_y, enemy_score, clock, player_score = state
        return f"You are at position {player_x, player_y}, your opponent is at position {enemy_x, enemy_y}, " \
               f"your oppoent's score is {enemy_score}, your score is {player_score}."



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
        return "The goal is to knock out your opponent."

    def translate_terminate_state(self, state, episode_len, max_episode_len):
        return ""

    def translate_potential_next_state(self, state, action):
        return ""

    def describe_game(self):
        return "In the Boxing game, you fight an opponent in a boxing ring. You score points for hitting the opponent. " \
               f"There are {self.args.frameskip} frames per step and the action stickes for the skipping frames. " if self.args.frameskip>0 else "" \
               "If you score 100 points, your opponent is knocked out. Scoring Points: When you get near enough to your opponent to throw a punch." \
               " Each move action moves yourself in the corresponding direction. Each punch moves your opponent slightly back and away from the punch." \
               " If you punch him to the ropes, he can't easily duck the next punch, " \
               "and you can set up a real scoring barrage. But don't get caught on the ropes yourself! Knock out your opponent!" 

    def describe_action(self):
        return "Type '1' for NOOP (no operation), '2' to hit your opponent, " \
               "'3' to move up, '4' to move right, '5' to move left, '6' to move down, '7' to move up and right, " \
               "'8' to move up and left, '9' to move down and right, '10' to move down and left, '11' to hit your opponent and move up, " \
               "'12' to hit your opponent and move right, '13' to hit your opponent and move left, '14' to hit your opponent and move down, " \
               "'15' to hit your opponent and move up and right, '16' to hit your opponent and move up and left, '17' to hit your opponent and move down and right, " \
               "or '18' to hit your opponent and move down and left. Ensure you only provide the action number " \
               "from the valid action list, i.e., [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]."


class TransitionTranslator(ObsTranslator):
    def translate(self, infos, is_current=False):
        descriptions = []
        if is_current:
            state_desc = ObsTranslator().translate(infos[-1]['state'])
            return state_desc
        for i, info in enumerate(infos):
            assert 'state' in info, "info should contain state information"

            state_desc = ObsTranslator().translate(info['state'])
            if info['action'] == 1:
                action_desc = f"Take Action: 'Do nothing'"
            elif info['action'] == 2:
                action_desc = f"Take Action: 'Hit your opponent'"
            elif info['action'] == 3:
                action_desc = f"Take Action: 'Move up'"
            elif info['action'] == 4:
                action_desc = f"Take Action: 'Move right'"
            elif info['action'] == 5:
                action_desc = f"Take Action: 'Move left'"
            elif info['action'] == 6:
                action_desc = f"Take Action: 'Move down'"
            elif info['action'] == 7:
                action_desc = f"Take Action: 'Move up-right'"
            elif info['action'] == 8:
                action_desc = f"Take Action: 'Move up-lefr'"
            elif info['action'] == 9:
                action_desc = f"Take Action: 'Move down-right'"
            elif info['action'] == 10:
                action_desc = f"Take Action: 'Move down-left'"
            elif info['action'] == 11:
                action_desc = f"Take Action: 'Hit your opponent and move up'"
            elif info['action'] == 12:
                action_desc = f"Take Action: 'Hit your opponent and move right'"
            elif info['action'] == 13:
                action_desc = f"Take Action: 'Hit your opponent and move left'"
            elif info['action'] == 14:
                action_desc = f"Take Action: 'Hit your opponent and move down'"
            elif info['action'] == 15:
                action_desc = f"Take Action: 'Hit your opponent and move up-right'"
            elif info['action'] == 16:
                action_desc = f"Take Action: 'Hit your opponent and move up-left'"
            elif info['action'] == 17:
                action_desc = f"Take Action: 'Hit your opponent and move down-right'"
            else:
                action_desc = f"Take Action: 'Hit your opponent and move down-left'"
            reward_desc = f"Result: Reward of {info['reward']}, "
            next_state_desc = ObsTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\n {action_desc} \n {reward_desc} \n Transit to {next_state_desc}")
        return descriptions
