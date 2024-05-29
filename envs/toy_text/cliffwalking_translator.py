class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        state = int(state)
        nrows = 12
        current_row = state // nrows
        current_col = state % nrows
        return f"The You are at location ({current_row}, {current_col}) in the grid world."

class GameDescriber:
    def __init__(self, args):
        self.is_only_local_obs = args.is_only_local_obs == 1
        self.max_episode_len = args.max_episode_len
        self.action_desc_dict = {
            1: "Move up",
            2: "Move right",
            3: "Move down",
            4: "Move left",
        }
        self.reward_desc_dict = {
            -100: "which is a cliff and lets him receive -100 reward",
            -1: "which lets him receive -1 reward"
        }

    def describe_goal(self):
        return (
            f"The goal is to navigate from the starting point to an target {'which locates at (3,11)' if not self.is_only_local_obs else ''}, while avoiding the cliff, in as few steps as possible."
        )

    def translate_terminate_state(self, state, episode_len, max_episode_len): 
        state = int(state)
        nrows = 12
        current_row = state // nrows
        current_col = state % nrows
        if current_row == 3 and current_col == 11:
            return f"The player reaches the goal location ({current_row}, {current_col}) in the grid world."
        else: 
            return f"The game ends with {episode_len} steps and the player does not reach the goal."

    def translate_potential_next_state(self, state, action):
        state = int(state)
        nrows = 12
        current_row = state // nrows
        current_col = state % nrows
        action = str(action)
        if action == '1':
            current_row -= 1
        elif action == '2':
            current_col += 1
        elif action == '3':
            current_row += 1
        elif action == '4':
            current_col -= 1
        return f"He tries to step into location ({current_row}, {current_col}),"

            
    def describe_game(self):
        return (
            "Cliff walking is a task in which you "
            f"control a player navigating a '4x12' grid world. The ('x', 'y') coordinate indicates the position at row 'x' and column 'y'. The player "\
            f"{'starts at the bottom-left corner of the grid,locating at (3,0). The player' if not self.is_only_local_obs else ''} "\
            "needs to find a goal location while avoiding "\
            f"cliffs {'(Transversal interval from (3, 1) to (3, 10)' if not self.is_only_local_obs else ''}. The player can choose from 4 actions: move up, "\
            "move right, move down, or move left. If the player takes an action at ('x', 'y'), he tries to move to ('a', 'b'). "\
            f"Rules: \n 1. If ('a', 'b') is a cliff, the player incurs a large penalty of -100, and is reset to the starting position. \n 2. If ('a', 'b') issafe or towards the grid boundary, results in a small penalty of -1. If ('a', 'b') is outside the grid's boundaries, it does not change position but still receive the -1 penalty. \n 3. The game ends when the ('a', 'b') is the goal or {self.max_episode_len} actions are performed."
            # f"Rules: \n 1.  If ('a', 'b') is a cliff, they incur a large penalty of -100, and are reset to the starting position. \n 2. A regular move, whether safe or towards the grid boundary, results in a small penalty of -1. If the player tries to move outside the grid's boundaries, it does not change position but still receive the -1 penalty. \n 3. The game ends when the player successfully reaches the goal or takes {self.max_episode_len} actions."
        )
            # "For each regular move, the player receives a -1 penalty, suggesting a non-cliff space for the stepping location. For a move that leads the player stepping into a cliff, the player receives a -100 penalty and return to the starting location. The game ends "
            # f"The game ends when the player reaches the goal or takes  {self.max_episode_len} actions."

    def describe_action(self):
        return (
            "Type a number to indicate the action. For current position ('x', 'y'), the action means the player try to step into the next position. Type '1' to move up, which means trying to step into ('x-1', 'y'), '2' to move right, which means ('x', 'y+1'), "
            "'3' to move down, which means ('x+1', 'y'), or '4' to move left, which means ('x', 'y-1'). Ensure you only provide "
            "the action number from the valid action list, i.e., [1, 2, 3, 4]."
        )


class TransitionTranslator(ObsTranslator):
    def translate(self, infos, is_current=False):
        descriptions = []
        if is_current:
            state_desc = ObsTranslator().translate(infos[-1]['state'])
            return state_desc
        for i, info in enumerate(infos):
            assert 'state' in info, "info should contain state information"

            state_desc = ObsTranslator().translate(info['state'])
            action_directions = ['up', 'right', 'down', 'left']
            action_desc = f"Take Action: Move {action_directions[info['action']-1]} ({info['action']})."
            reward_desc = f"Result: Reward of {info['reward']}, "
            next_state_desc = ObsTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\n {action_desc} \n {reward_desc} \n Transit to {next_state_desc}")
        return descriptions