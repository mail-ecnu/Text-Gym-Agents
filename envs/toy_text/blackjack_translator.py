class ObsTranslator:
    def __init__(self):
        pass

    def translate(self, state):
        player_sum, dealer_showing, usable_ace = state
        usable_ace_text = "yes" if usable_ace else "no"
        res = (f"The player's current sum is {player_sum}, the dealer is showing {dealer_showing}, "
               f"and the player has a usable ace: {usable_ace_text}.")
        return res

class GameDescriber:
    def __init__(self, args):
        self.is_only_local_obs = args.is_only_local_obs == 1
        self.max_episode_len = args.max_episode_len
        self.action_desc_dict = {
            1: "Stick",
            2: "Hit"
        }
        self.reward_desc_dict = {
            1: "which lets him win the game and receive 1 reward",
            -1: "which lets him lose the game and receive -1 reward",
            0: "which lets him draw the game and receive 0 reward"
        }

    def describe_goal(self):
        return "The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21."
        
    def translate_terminate_state(self, state, episode_len, max_episode_len): 
        return '' 
    
    def translate_potential_next_state(self, state, action): 
        return '' 
        
    def describe_game(self):
        return ("In the game of Blackjack, the main aim is to obtain a higher card sum than the dealer, but not higher "
                "than 21. Face cards count as 10, numerical cards hold their value, and aces can count either as "
                "1 or 11. The game starts with the dealer having one face-up and one face-down card, while the player has "
                "two face-up cards. The player can either choose to 'hit' (add a card) or 'stick' (stop receiving cards). "
                "The game ends when the player or the dealer busts or when both the player and dealer are finished "
                "drawing cards.")

    def describe_action(self):
        return ("Type '1' to stick (stop receiving cards) or '2' to hit (add a card). "
                "Ensure you only provide the action number from the valid action list, i.e., [1, 2] in json format.")

class TransitionTranslator(ObsTranslator):
    def translate(self, infos, is_current=False):
        descriptions = []
        if is_current:
            state_desc = ObsTranslator().translate(infos[-1]['state'])
            return state_desc
        for i, info in enumerate(infos):
            assert 'state' in info, "info should contain state information"

            state_desc = ObsTranslator().translate(info['state'])
            action_desc = f"Take Action: {'Hit' if info['action'] == 2 else 'Stick'} ({info['action']})."
            reward_desc = f"Result: Reward of {info['reward']}, "
            next_state_desc = ObsTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}.\n {action_desc} \n {reward_desc} \n Transit to {next_state_desc}")
        return descriptions
