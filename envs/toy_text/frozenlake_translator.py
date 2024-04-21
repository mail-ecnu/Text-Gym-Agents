class BasicLevelTranslator:
    def __init__(self):
        pass

    def translate(self, state, nrow=4, ncol=4):
        row, col = state // nrow, state % ncol
        res = f"The current position of the player is at row {row}, column {col}."
        return res

class GameDescriber:
    def __init__(self, args):
        self.is_only_local_obs = args.is_only_local_obs == 1
        self.max_episode_len = args.max_episode_len
        self.action_desc_dict = {
            1: "Move left",
            2: "Move down",
            3: "Move right",
            4: "Move up",
        }
        self.reward_desc_dict = {
            1: "which lets him reach the goal and receive 1 reward",
            0: "which lets him receive 0 reward"
        }

    def describe_goal(self):
        return f"The goal is to navigate across the frozen lake and reach the goal position {'located at (3,3)' if not self.is_only_local_obs else ''}  without falling into any holes{', which are located at (1,1), (1,3), (2,3) and (3,0)' if not self.is_only_local_obs else ''}."

    def translate_terminate_state(self, state, episode_len, max_episode_len): 
        state = int(state)
        nrows = 4
        current_row = state // nrows
        current_col = state % nrows
        if current_row == 3 and current_col == 3:
            return f"The player reaches the goal location ({current_row}, {current_col}) in the grid world."
        else: 
            if (current_row, current_col) in [(1,1), (1, 3), (2,3), (3, 0)]:
                return f"The game ends due to step into a hole locating at {(current_row, current_col)}."
            else:
                return f"The game ends due to reach the max episode length {episode_len} and the player does not reach the goal."

    def translate_potential_next_state(self, state, action):
        state = int(state)
        nrows = 4
        current_row = state // nrows
        current_col = state % nrows
        action = str(action)
        if action == '1':
            current_col -= 1
        elif action == '2':
            current_row += 1
        elif action == '3':
            current_col += 1
        elif action == '4':
            current_row -= 1
        return f"He tries to step into location ({current_row}, {current_col}),"

    def describe_game(self):
        return "In the FrozenLake game, the player starts at the start position of the grid and tries to reach the" \
               f" goal position {'located at (3,3)' if not self.is_only_local_obs else ''}. There are holes which the player must avoid{'. These holes are located at (1,1), (1,3), (2,3) and (3,0)' if not self.is_only_local_obs else ''}. The frozen lake is " \
               "slippery, meaning that the player might not always move in the intended direction. The game ends" \
               " when the player reaches the goal or falls into a hole."

    def describe_action(self):
        return ("For current position ('x', 'y'), the action means the player try to step into the next position. The possible actions are:" \
                "\n '1': Move left, which means ('x', 'y-1'), " \
                "\n '2': Move down, which means ('x+1', 'y')," \
                "\n '3': Move right, which means ('x', 'y+1')," \
                "\n '4': Move up, which means trying to step into ('x-1', 'y')." \
                " Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].")

class BasicStateSequenceTranslator(BasicLevelTranslator):
    def translate(self, infos, is_current=False):
        descriptions = []
        if is_current:
            state_desc = BasicLevelTranslator().translate(infos[-1]['state'])
            return state_desc
        for i, info in enumerate(infos):
            assert 'state' in info, "info should contain state information"

            state_desc = BasicLevelTranslator().translate(info['state'])
            action_directions = ['left', 'down', 'right', 'up']
            action_desc = f"Take Action: Move {action_directions[info['action']-1]} ({info['action']})."
            reward_desc = f"Result: Reward of {info['reward']}, "
            next_state_desc = BasicLevelTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\n {action_desc} \n {reward_desc} \n Transit to {next_state_desc}")
        return descriptions
