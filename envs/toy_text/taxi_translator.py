class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        # Decode the state
        state = state % 500
        taxi_row, taxi_col, passenger_location, destination = self.decode_state(state)

        taxi_location = f"Taxi is at Row {taxi_row}, Col {taxi_col}."
        if passenger_location == 4:
            passenger_location_text = "In taxi"
        else:
            passenger_location_text = ["Red", "Green", "Yellow", "Blue"][passenger_location]

        passenger_desc = f"The passenger is at the {passenger_location_text} location."

        destination_text = ["Red", "Green", "Yellow", "Blue"][destination]
        destination_desc = f"The passenger wants to go to the {destination_text} location."

        return f"{taxi_location} {passenger_desc} {destination_desc}"

    def decode_state(self, state):
        out = []
        out.append(state // 100)
        state = state % 100
        out.append(state // 20)
        state = state % 20
        out.append(state // 4)
        out.append(state % 4)
        return tuple(out)


class GameDescriber:
    def __init__(self, args):
        self.is_only_local_obs = args.is_only_local_obs == 1
        self.max_episode_len = args.max_episode_len
        self.action_desc_dict = {
            1: "Move down", 
            2: "Move up",
            3: "Move right",
            4: "Move left", 
            5: "Pickup passenger",
            6: "drop off passenger"
        }
        self.reward_desc_dict = {
            20: "which lets him deliver the passenger successfully and receive 20 reward",
            -10: "which lets him execute 'pickup' or 'drop-off' actions illegally and receive -10 reward",
            -1: "which lets him receive -1 reward"
        }

    def describe_goal(self):
        return "The goal is to navigate the taxi to the passenger, pick them up, and drop them off at their destination as efficiently as possible."

    def translate_terminate_state(self, state, episode_len, max_episode_len): 
        return ""

    def translate_potential_next_state(self, state, action):
        return ""

    def describe_game(self):
        return "In the Taxi Problem, you control a taxi in a 5x5 grid world with four designated pick-up and drop-off locations (Red, Green, Yellow, and Blue). " \
               "The taxi starts off at a random square and the passenger at one of the designated locations. " \
               "The goal is to move the taxi to the passenger's location, pick up the passenger, move to the passenger's desired destination, and drop off the passenger. " \
               "The episode ends once the passenger is dropped off. " \
               "Rewards include a positive reward for successfully dropping off the passenger at the correct location, " \
               "a negative reward for incorrect attempts to pick-up/drop-off the passenger, " \
               "or negative rewards for each step where another reward is not received. " \
               "The game terminates once the passenger is dropped off, or if the episode reaches the 200 time step limit." + \
               """There are four designated pick-up and drop-off locations (Red, Green, Yellow, and Blue). Red location is at (0, 0) while Green, Yellow, and Blue locations are at (0, 4), (4, 0), (4, 3), respectively. There are walls/obstacles in the environment that the taxi cannot pass through. The walls are located at:
                Vertical walls:
                Between rows 0 and 1, column 1
                Between rows 3 and 4, column 1
                Between rows 0 and 4, column 3
                Horizontal walls:
                Between columns 0 and 1, row 0
                Between columns 3 and 4, row 0
                Between columns 0 and 1, row 4
                Between columns 3 and 4, row 4
                These walls divide the grid into separate areas, and the taxi must navigate around them to reach the pickup and drop-off locations. 
                """

    def describe_action(self):
        return "Your Next Move: \n Please choose an action. Type '1' to move south (down), '2' to move north (up), '3' to move east (right), " \
               "'4' to move west (left), '5' to pick up the passenger or '6' to drop off the passenger. " \
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
            action_desc = {1: 'move south', 2: 'move north', 3: 'move east', 4: 'move west', 5: 'pick up passenger', 6: 'drop off passenger'}[info['action']]
            action_desc_text = f"Take Action: {action_desc} ({info['action']})."

            reward_desc = f"Result: Reward of {info['reward']}, "
            next_state_desc = ObsTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\n {action_desc_text} \n {reward_desc} \n Transit to {next_state_desc}")
        return descriptions
