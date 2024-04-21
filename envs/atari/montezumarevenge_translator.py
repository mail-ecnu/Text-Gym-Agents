class ObsTranslator:
    def __init__(self):
        self.player_direction_map = {
            72: "facing left",
            40: "facing left, climbing down ladder/rope",
            24: "facing left, climbing up ladder/rope",
            128: "facing right",
            32: "facing right, climbing down ladder/rope",
            16: "facing right, climbing up ladder/rope",
        }

    def translate(self, state):
        (
            room_number, player_x, player_y, player_direction, enemy_skull_x, enemy_skull_y,
            key_monster_x, key_monster_y, level, num_lives, items_in_inventory_count,
            room_state, score_0, score_1, score_2
        ) = state
        
        player_dir = self.player_direction_map.get(player_direction, "unknown direction")
        picked_up_items = "None"
        
        if items_in_inventory_count > 0:
            items = [
                ("Key", "Opens locked doors.", 1),
                ("Ankh", "Freeze enemies.", 2),
                ("Gem", "Extra bonus points.", 4),
                ("Torch", "Lights up dark rooms.", 8),
                ("Sword", "Vanquishes certain enemies.", 16),
            ]
            
            picked_up_items = ""
            for name, desc, val in items:
                if items_in_inventory_count & val == val:
                    picked_up_items += f"{name} ({desc}), "
            picked_up_items = picked_up_items[:-2]
        
        res = f"""Room Number:                                  {room_number}
Player Position:                             ({player_x}, {player_y})
Player Direction:                            {player_dir}
Enemy Skull Position:                       ({enemy_skull_x}, {enemy_skull_y})
Key Monster Position:                       ({key_monster_x}, {key_monster_y})
Level:                                           {level}
Remaining Lives:                             {num_lives}
Items in Inventory:                          {picked_up_items if picked_up_items else "None"}
Room State (Mapped Based on Room Number): {room_state}
Current Score:                                {score_0}{score_1}{score_2}\n"""
        return res


class GameDescriber:
    def __init__(self, args):
        self.is_only_local_obs = args.is_only_local_obs == 1
        self.max_episode_len = args.max_episode_len
        self.action_desc_dict = {
        }
        self.reward_desc_dict = {
        }

    def describe_goal(self):
        return ("The goal is to guide PANAMA JOE safely to reach Montezuma's fantastic treasure. "
                "Avoid danger, collect special tools and rewards, and navigate through the chambers of the emperor's fortress.")

    def describe_game(self):
        return ("""In Montezuma's Revenge, you control a fearless adventurer named PANAMA JOE who aims to navigate through a maze 
of death-dealing chambers within Emperor Montezuma's fortress. PANAMA JOE can walk, climb, and jump in the game. In each room of the 
maze, there are several dangers, including various creatures such as skulls, snakes, spiders, and bats, as well as several deadly room 
fixtures like fire pits, conveyor belts, disappearing floors, laser gates, floor spikes, and laser walls. 

PANAMA JOE can act on several elements within the game environment. Some items in the game are: 
1. Keys: Essential to open locked doors, allowing access to other rooms and deeper exploration.
2. Ankhs: Freeze all Killer Creatures in the room for 6.5 seconds, during which they can't move or kill.
3. Gems: Extra bonus points when collected.
4. Torches: Light up dark rooms, making it easier to navigate through threats.
5. Swords: Used to defeat certain enemies, by contact with the tip of the sword.

The game's ultimate goal is to reach the fabulous Treasure Room containing Montezuma's treasure while amassing as many points as 
possible and keeping PANAMA JOE alive through the challenges. The game ends when you lose all of your PANAMA JOEs, with a maximum 
of 6 lives.""")
    
    def translate_terminate_state(self, state, episode_len, max_episode_len): 
        return ""
    
    def translate_potential_next_state(self, state, action):
        return ""

    def describe_action(self):
        actions = {
            1:  "No Operation",
            2:  "Move Right",
            3:  "Move Left",
            4:  "Move Down",
            5:  "Move Up",
            6:  "Move Right + Climb Down",
            7:  "Move Left + Climb Down",
            8:  "Move Right + Climb Up",
            9:  "Move Left + Climb Up",
            10:  "Jump",
            11: "Jump Right",
            12: "Jump Left",
            13: "Jump Down",
            14: "Jump Up",
            15: "Jump Right + Climb Down",
            16: "Jump Left + Climb Down",
            17: "Jump Right + Climb Up",
            18: "Jump Left + Climb Up",
        }

        description = ""
        for action_number, action_name in actions.items():
            description += f"{action_number}: {action_name}\n"

        description += "Please choose an action from the list above."
        return description

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
            action_desc = f'Take Action: {["No Operation", "Move Right", "Move Left", "Move Down", "Move Up", "Move Right + Climb Down", "Move Left + Climb Down", "Move Right + Climb Up", "Move Left + Climb Up", "Jump","Jump Right", "Jump Left", "Jump Down", "Jump Up", "Jump Right + Climb Down", "Jump Left + Climb Down", "Jump Right + Climb Up", "Jump Left + Climb Up"][info["action"]]} ({info["action"]}).'
            reward_desc = f"Result: Reward of {info['reward']}"
            next_state_desc = ObsTranslator().translate(info['next_state'])
            descriptions.append(f"{state_desc}\n"
                                f"{action_desc}\n"
                                f"{reward_desc}\n"
                                f"Transit to {next_state_desc}\n")

        return descriptions
