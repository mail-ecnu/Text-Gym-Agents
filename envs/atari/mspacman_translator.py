class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        x, y = state[8], state[9]
        ghosts = [(state[0], state[4]), (state[1], state[5]), (state[2], state[6]), (state[3], state[7])]
        ghost_directions = ["UP", "RIGHT", "LEFT", "DOWN"]

        direction = ghost_directions[int(state[13])]
        eaten_dots = state[14]
        score = state[15]
        lives = state[16]
        ghosts_count = state[12]

        fruit_x, fruit_y = state[10], state[11]
        fruit_present = fruit_x != 0 or fruit_y != 0

        player_state = f"Ms. Pac-Man is at position ({x}, {y}), facing {direction} with {lives} lives left. {eaten_dots} dots have been eaten so far and the current score is {score}. The game has {ghosts_count} ghosts."

        ghost_states = []
        for i, (gx, gy) in enumerate(ghosts):
            ghost_name = ["Sue", "Inky", "Pinky", "Blinky"][i]
            ghost_states.append(f"{ghost_name} the ghost is at position ({gx}, {gy})")
        ghost_state_str = " ".join(ghost_states)
        
        fruit_state = f"A fruit is present at position ({fruit_x}, {fruit_y})" if fruit_present else "No fruit is currently present on the screen."

        result = f"{player_state} {fruit_state} {ghost_state_str}"
        return result


class GameDescriber:
    def __init__(self, args):
        self.is_only_local_obs = args.is_only_local_obs == 1
        self.max_episode_len = args.max_episode_len
        self.action_desc_dict = {
        }
        self.reward_desc_dict = {
        }

    def describe_goal(self):
        return "The goal of Ms. Pac-Man is to score as many points as possible while avoiding the ghosts."

    def describe_game(self):
        return "In the Ms. Pac-Man game, you control Ms. Pac-Man, moving around a maze, eating dots to score points. "\
               "There are also special bonus items, such as fruit and pretzels, that appear for a limited time and award "\
               "extra points. Ghosts chase Ms. Pac-Man around the maze, but she can eat an energy pill to temporarily "\
               "turn the ghosts vulnerable and eat them for extra points. The game ends when you lose all your lives. "\
               "Score 10,000 points and earn a bonus life."
    
    def translate_terminate_state(self, state, episode_len, max_episode_len): 
        return ""
    
    def translate_potential_next_state(self, state, action):
        return ""

    def describe_action(self):
        return "Your Next Move: \n Please choose an action. Each value corresponds to a directional input as follows: "\
               "1 - NOOP, 2 - UP, 3 - RIGHT, 4 - LEFT, 5 - DOWN, 6 - UPRIGHT, 7 - UPLEFT, 8 - DOWNRIGHT, 9 - DOWNLEFT. "\
               "Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6, 7, 8, 9]."

class TransitionTranslator(ObsTranslator):
    def __init__(self):
        super().__init__()

    def translate(self, infos, is_current=False):
        descriptions = []
        if is_current:
            state_desc = ObsTranslator().translate(infos[-1]['state'])
            return state_desc
        for i, info in enumerate(infos):
            assert 'state' in info, "info should contain state information"

            state_desc = ObsTranslator().translate(info['state'])
            action_desc = f"Take Action: {['NOOP', 'UP', 'RIGHT', 'LEFT', 'DOWN', 'UPRIGHT', 'UPLEFT', 'DOWNRIGHT', 'DOWNLEFT'][info['action']]} ({info['action']})."
            reward_desc = f"Result: Reward of {info['reward']}, "
            next_state_desc = ObsTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\\n {action_desc} \\n {reward_desc} \\n Transit to {next_state_desc}")
        return descriptions
