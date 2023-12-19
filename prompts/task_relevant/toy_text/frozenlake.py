class ACT:
    def __init__(self,):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
            State description: Current Game State: The current position of the player is at row 0, column 1.
            Goal description: The goal is to navigate across the frozen lake and reach the goal position located at (3,3) without falling into any holes, which are located at (1,1), (1,3), (2,3) and (0,3).
            Action description: Your Next Move: 
            Please choose an action. The possible actions are:
            '1': Move left (Decrease the horizontal coordinate by 1)
            '2': Move down (Increase the vertical coordinate by 1)
            '3': Move right (Increase the horizontal coordinate by 1)
            '4': Move up (Decrease the vertical coordinate by 1). Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            So the final answer is: move right (Action 3).
                    """
            },
            {
                "question":
                    """
            State description: Current Game State: The current position of the player is at row 1, column 0.
            Goal description: The goal is to navigate across the frozen lake and reach the goal position located at (3,3) without falling into any holes, which are located at (1,1), (1,3), (2,3) and (0,3).
            Action description: Your Next Move: 
            Please choose an action. The possible actions are:
            '1': Move left (Decrease the horizontal coordinate by 1)
            '2': Move down (Increase the vertical coordinate by 1)
            '3': Move right (Increase the horizontal coordinate by 1)
            '4': Move up (Decrease the vertical coordinate by 1). Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            So the final answer is: move down (Action 2).
                    """
            }
        ]


class COT:
    def __init__(self,):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
            State description: Current Game State: The current position of the player is at row 0, column 1.
            Goal description: The goal is to navigate across the frozen lake and reach the goal position located at (3,3) without falling into any holes, which are located at (1,1), (1,3), (2,3) and (0,3).
            Action description: Your Next Move: 
            Please choose an action. The possible actions are:
            '1': Move left (Decrease the horizontal coordinate by 1)
            '2': Move down (Increase the vertical coordinate by 1)
            '3': Move right (Increase the horizontal coordinate by 1)
            '4': Move up (Decrease the vertical coordinate by 1). Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            The player is currently located at (0,1) on the frozen lake, with the goal of reaching the position at (3,3) without falling into any holes. The holes are located at (1,1), (1,3), (2,3), and (0,3).
            The player's task is to navigate across the frozen lake while avoiding the holes and reach the goal position at (3,3).
            Given the current position of the player and the positions of the holes, the optimal action for the player in this state is to move right - as moving down would result in falling into a hole, moving up would result in encountering a wall and moving left will lead the player away from the goal.
            So the final answer is: move right (Action 3).
            """
            },
            {
                "question":
                    """
            State description: Current Game State: The current position of the player is at row 1, column 0.
            Goal description: The goal is to navigate across the frozen lake and reach the goal position located at (3,3) without falling into any holes, which are located at (1,1), (1,3), (2,3) and (0,3).
            Action description: Your Next Move: 
            Please choose an action. The possible actions are:
            '1': Move left (Decrease the horizontal coordinate by 1)
            '2': Move down (Increase the vertical coordinate by 1)
            '3': Move right (Increase the horizontal coordinate by 1)
            '4': Move up (Decrease the vertical coordinate by 1). Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            The player is currently located at (1,0) on the frozen lake, with the goal of reaching the position at (3,3) without falling into any holes. The holes are located at (1,1), (1,3), (2,3), and (0,3).
            The player's task is to navigate across the frozen lake while avoiding the holes and reach the goal position at (3,3).
            Given the current position of the player and the positions of the holes, the optimal action for the player in this state is to move down - as moving right would result in falling into a hole, moving up would lead the player away from the goal, and moving left is not possible as it would result in encountering a wall.
            So the final answer is: move down (Action 2).
            """
            }
        ]


class PAL:
    def __init__(self) -> None:
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [{
                "question":
                    """
            State description: Current Game State: The current position of the player is at row 0, column 1.
            Goal description: The goal is to navigate across the frozen lake and reach the goal position located at (3,3) without falling into any holes, which are located at (1,1), (1,3), (2,3) and (0,3).
            Action description: Your Next Move: 
            Please choose an action. The possible actions are:
            '1': Move left (Decrease the horizontal coordinate by 1)
            '2': Move down (Increase the vertical coordinate by 1)
            '3': Move right (Increase the horizontal coordinate by 1)
            '4': Move up (Decrease the vertical coordinate by 1). Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            from collections import deque
            def bfs_find_best_action(player_position, goal_position, holes):
                queue = deque([(player_position, [])])
                visited = set()

                while queue:
                    current_position, path = queue.popleft()

                    if current_position == goal_position:
                        if path:
                            return path[0]
                        return None

                    if current_position in visited or current_position in holes:
                        continue

                    visited.add(current_position)

                    for i, next_action in enumerate([(0, -1), (1, 0), (0, 1), (-1, 0)]):
                        i += 1
                        next_position = cal_next_position(current_position, next_action)

                        # Check if next move is within the grid
                        if 0 <= next_position[0] < 4 and 0 <= next_position[1] < 4:
                            new_path = path + [i]
                            queue.append((next_position, new_path))

            def cal_next_position(p, a):
                return (p[0] + a[0], p[1] + a[1])

            player_position = (0, 1)
            goal_position = (3, 3)
            holes = [(1, 1), (1, 3), (2, 3), (0, 3)]

            action = bfs_find_best_action(player_position, goal_position, holes)

            action_description = dict()
            action_description[1] = "Move left (Decrease the horizontal coordinate by 1)"
            action_description[2] = "Move down (Increase the vertical coordinate by 1)"
            action_description[3] = "Move right (Increase the horizontal coordinate by 1)"
            action_description[4] = "Move up (Decrease the vertical coordinate by 1)"

            print("The optimal action is : "  + "Action " + str(action))
            The optimal action is : Action 3
            """
            },
            {
                "question":
                    """
                State description: Current Game State: Taxi is at Row 1, Col 2. The passenger is at the Yellow location. The passenger wants to go to the Red location.
                Goal description: The goal is to navigate the taxi to the passenger, pick them up, and drop them off at their destination as efficiently as possible.
                Action description: Your Next Move: Please choose an action. Type '1' to move south (down), '2' to move north (up), '3' to move east (right), '4' to move west (left), '5' to pick up the passenger or '6' to drop off the passenger. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6].
                """,
                "answer":
                    """
                from collections import deque
                def bfs_find_best_action(player_position, goal_position, holes):
                    queue = deque([(player_position, [])])
                    visited = set()

                    while queue:
                        current_position, path = queue.popleft()

                        if current_position == goal_position:
                            if path:
                                return path[0]
                            return None

                        if current_position in visited or current_position in holes:
                            continue

                        visited.add(current_position)

                        for i, next_action in enumerate([(0, -1), (1, 0), (0, 1), (-1, 0)]):
                            i += 1
                            next_position = cal_next_position(current_position, next_action)

                            # Check if next move is within the grid
                            if 0 <= next_position[0] < 4 and 0 <= next_position[1] < 4:
                                new_path = path + [i]
                                queue.append((next_position, new_path))

                def cal_next_position(p, a):
                    return (p[0] + a[0], p[1] + a[1])

                player_position = (1, 0)
                goal_position = (3, 3)
                holes = [(1, 1), (1, 3), (2, 3), (0, 3)]

                action = bfs_find_best_action(player_position, goal_position, holes)

                action_description = dict()
                action_description[1] = "Move left (Decrease the horizontal coordinate by 1)"
                action_description[2] = "Move down (Increase the vertical coordinate by 1)"
                action_description[3] = "Move right (Increase the horizontal coordinate by 1)"
                action_description[4] = "Move up (Decrease the vertical coordinate by 1)"

                print("The optimal action is : "  + "Action " + str(action))
                The optimal action is : Action 2
            """
            }]


class CONSISTENCY:
    def __init__(self) -> None:
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [{
                "question":
                    """
            State description: Current Game State: The current position of the player is at row 0, column 1.
            Goal description: The goal is to navigate across the frozen lake and reach the goal position located at (3,3) without falling into any holes, which are located at (1,1), (1,3), (2,3) and (0,3).
            Action description: Your Next Move: 
            Please choose an action. The possible actions are:
            '1': Move left (Decrease the horizontal coordinate by 1)
            '2': Move down (Increase the vertical coordinate by 1)
            '3': Move right (Increase the horizontal coordinate by 1)
            '4': Move up (Decrease the vertical coordinate by 1). Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            The player is currently located at (0,1) on the frozen lake, with the goal of reaching the position at (3,3) without falling into any holes. The holes are located at (1,1), (1,3), (2,3), and (0,3).
            The player's task is to navigate across the frozen lake while avoiding the holes and reach the goal position at (3,3).
            Given the current position of the player and the positions of the holes, the optimal action for the player in this state is to move right - as moving down would result in falling into a hole, moving up would result in encountering a wall and moving left will lead the player away from the goal.
            So the final answer is: move right (Action 3).
            """
            },
            {
                "question":
                    """
            State description: Current Game State: The current position of the player is at row 1, column 0.
            Goal description: The goal is to navigate across the frozen lake and reach the goal position located at (3,3) without falling into any holes, which are located at (1,1), (1,3), (2,3) and (0,3).
            Action description: Your Next Move: 
            Please choose an action. The possible actions are:
            '1': Move left (Decrease the horizontal coordinate by 1)
            '2': Move down (Increase the vertical coordinate by 1)
            '3': Move right (Increase the horizontal coordinate by 1)
            '4': Move up (Decrease the vertical coordinate by 1). Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            The player is currently located at (1,0) on the frozen lake, with the goal of reaching the position at (3,3) without falling into any holes. The holes are located at (1,1), (1,3), (2,3), and (0,3).
            The player's task is to navigate across the frozen lake while avoiding the holes and reach the goal position at (3,3).
            Given the current position of the player and the positions of the holes, the optimal action for the player in this state is to move down - as moving right would result in falling into a hole, moving up would lead the player away from the goal, and moving left is not possible as it would result in encountering a wall.
            So the final answer is: move down (Action 2).
            """
            }]


class SELFASK:
    def __init__(self) -> None:
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [{
                "question":
                    """
            State description: Current Game State: The current position of the player is at row 0, column 1.
            Goal description: The goal is to navigate across the frozen lake and reach the goal position located at (3,3) without falling into any holes, which are located at (1,1), (1,3), (2,3) and (0,3).
            Action description: Your Next Move: 
            Please choose an action. The possible actions are:
            '1': Move left (Decrease the horizontal coordinate by 1)
            '2': Move down (Increase the vertical coordinate by 1)
            '3': Move right (Increase the horizontal coordinate by 1)
            '4': Move up (Decrease the vertical coordinate by 1). Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            Are follow-up questions needed here: Yes.
            Follow up: What is the current location of the player?
            Intermediate answer: The current position of the player is at row 0, column 1, i.e., (0,1).
            Follow up: Where is the goal location?
            Intermediate answer: The goal position is located at row 3, column 3, i.e., (3,3).
            Follow up: Where are the obstacles (holes) located?
            Intermediate answer: The obstacles (holes) are located at (1,1), (1,3), (2,3), and (0,3).
            Follow up: Is there an ice hole or wall near the player?
            Intermediate answer: There is a wall above the player and an ice hole below.
            Follow up: What is the task of the player in its current state?
            Intermediate answer: The task of the player is to navigate across the frozen lake without falling into any holes and reach the goal position at (3,3).
            Follow up: What might be an optimal action for the player in its current state?
            Intermediate answer: The optimal action for the player might be to move right (Action 3), as moving down would result in falling into a hole, moving up would result in encountering a wall and moving left will lead the player away from the goal.
            So the final answer is: move right (Action 3).
            """
            },
            {
                "question":
                    """
            State description: Current Game State: The current position of the player is at row 1, column 0.
            Goal description: The goal is to navigate across the frozen lake and reach the goal position located at (3,3) without falling into any holes, which are located at (1,1), (1,3), (2,3) and (0,3).
            Action description: Your Next Move: 
            Please choose an action. The possible actions are:
            '1': Move left (Decrease the horizontal coordinate by 1)
            '2': Move down (Increase the vertical coordinate by 1)
            '3': Move right (Increase the horizontal coordinate by 1)
            '4': Move up (Decrease the vertical coordinate by 1). Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            Are follow-up questions needed here: Yes.
            Follow up: What is the current location of the player?
            Intermediate answer: The current position of the player is at row 1, column 0, i.e., (1,0).
            Follow up: Where is the goal location?
            Intermediate answer: The goal position is located at row 3, column 3, i.e., (3,3).
            Follow up: Where are the obstacles (holes) located?
            Intermediate answer: The obstacles (holes) are located at (1,1), (1,3), (2,3), and (0,3).
            Follow up: Is there an ice hole or wall near the player?
            Intermediate answer: There is a wall on the player's left side and an ice hole on the right side..
            Follow up: What is the task of the player in its current state?
            Intermediate answer: The task of the player is to navigate across the frozen lake without falling into any holes and reach the goal position at (3,3).
            Follow up: What might be an optimal action for the player in its current state?
            Intermediate answer: The optimal action for the player might be to move down (Action 2), as moving right would result in falling into a hole, moving left would result in encountering a wall and moving up will lead the player away from the goal.
            So the final answer is: move down (Action 2).
            """
            }]


class SPP:
    def __init__(self) -> None:
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [{
                "question":
                    """
        Use numbers and basic arithmetic operations (+ - * /) to obtain 24. You need to use all numbers, and each number can only be used once.
        Input: 6 12 1 1
        """,
                "answer":
                    """
        Participants: AI Assistant (you); Math Expert
        
        Start collaboration!
        
        Math Expert: Let's analyze the task in detail. You need to make sure that you meet the requirement, that you need to use exactly the four numbers (6 12 1 1) to construct 24. To reach 24, you can think of the common divisors of 24 such as 4, 6, 8, 3 and try to construct these first. Also you need to think of potential additions that can reach 24, such as 12 + 12.
        AI Assistant (you): Thanks for the hints! Here's one initial solution: (12 / (1 + 1)) * 6 = 24
        Math Expert: Let's check the answer step by step. (1+1) = 2, (12 / 2) = 6, 6 * 6 = 36 which is not 24! The answer is not correct. Can you fix this by considering other combinations? Please do not make similar mistakes.
        AI Assistant (you): Thanks for pointing out the mistake. Here is a revised solution considering 24 can also be reached by 3 * 8: (6 + 1 + 1) * (12 / 4) = 24.
        Math Expert: Let's first check if the calculation is correct. (6 + 1 + 1) = 8, 12 / 4 = 3, 8 * 3 = 24. The calculation is correct, but you used 6 1 1 12 4 which is not the same as the input 6 12 1 1. Can you avoid using a number that is not part of the input?
        AI Assistant (you): You are right, here is a revised solution considering 24 can be reached by 12 + 12 and without using any additional numbers: 6 * (1 - 1) + 12 = 24.
        Math Expert: Let's check the answer again. 1 - 1 = 0, 6 * 0 = 0, 0 + 12 = 12. I believe you are very close, here is a hint: try to change the "1 - 1" to "1 + 1".
        AI Assistant (you): Sure, here is the corrected answer:  6 * (1+1) + 12 = 24
        Math Expert: Let's verify the solution. 1 + 1 = 2, 6 * 2 = 12, 12 + 12 = 12. You used 1 1 6 12 which is identical to the input 6 12 1 1. Everything looks good!
        
        Finish collaboration!
        
        Final answer: 6 * (1 + 1) + 12 = 24
                   """
            },
            {
                "question":
                    """
        Write a poem that meets the following requirements: (1) the poem has seven lines and the first letters of each line forms the word "CHATGPT"; (2) the poem is about explaining what is a quantum computer. (3) the poem needs to be easy to understand by a ten years old kid.
        """,
                "answer":
                    """
        Participants: AI Assistant (you); Poet; Computer Scientist; Ten year old child
        
        Poet: Make sure that you write the poem with seven lines, and the first letters of the lines should be C, H, A, T, G, P, T.
        Computer Scientist: A quantum computer is an advanced computing device that uses the principles of quantum mechanics to process and store information. Unlike classical computers that use bits to represent information as 0s and 1s, quantum computers use quantum bits or qubits. Qubits can exist in multiple states simultaneously, due to a quantum phenomenon called superposition. You can consider using these information for the poem.
        Ten year old child: I hope the poem to be fun and easy to understanding. I don't want to see a lot of jargons or complicated concepts.
        AI Assistant (you): Thanks for the guidance! Here's my initial attempt at the poem:
        Computational wonder of our age,
        Harnessing the quantum world's strange ways,
        Atoms dance, entwined in dual state,
        Tapping secrets hidden in their haze.
        
        Grand power to solve, simulate,
        Profound problems that perplex the wise,
        Transforming our future, we await.
        
        Poet: Let's verify if the poem meets the requirements. The first letters are CHATGPT which is correct! And the poem rhymes well. Good job!
        Computer Scientist: Everything looks good to me!
        Ten year old child: I don't know what does perplex mean. Can you make the use of words easier to understand?
        AI Assistant (you): Sure, let me revise the poem by using more common words. Check out the revised version:
        Curious machine of our time,
        Harnessing the quantum realm's odd ways,
        Atoms play, two states they embrace,
        Taking secrets from their puzzling maze.
        
        Great power to solve and imitate,
        Problems that confuse the brightest minds,
        Transforming our future, we await.
        
        Poet: Let's check again if the poem meets the requirements. The first letters are C H A T G P T. And now the poem is more accessible to children. Everything looks good to me.
        Computer Scientist: Looking good!
        Ten year old child: I like this version a lot!
        
        Finish collaboration!
        
        Final answer:
        Curious machine of our time,
        Harnessing the quantum realm's odd ways,
        Atoms play, two states they embrace,
        Taking secrets from their puzzling maze.
        
        Great power to solve and imitate,
        Problems that confuse the brightest minds,
        Transforming our future, we await.
                   """
            }]

class REFLEXION:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: The current position of the player is at row 2, column 0.
                Goal description: The goal is to navigate across the frozen lake and reach the goal position located at (3,3) without falling into any holes, which are located at (1,1), (1,3), (2,3) and (0,3).
                Action description: Your Next Move: 
                Please choose an action. The possible actions are:
                '1': Move left (Decrease the horizontal coordinate by 1)
                '2': Move down (Increase the vertical coordinate by 1)
                '3': Move right (Increase the horizontal coordinate by 1)
                '4': Move up (Decrease the vertical coordinate by 1). Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                Your memory for the task below:
                Trial 0:
                In this environment, I was trying to reach the goal position without falling into any holes. However, I did not check the current position of the player before making a move. I should have checked the current position of the player before making a move. In the next trial, I will check the current position of the player before making a move.<|im_end|>
                Trial 1:
                In this environment, I am trying to reach the goal position without falling into any holes. I should check the current position of the player before making a move. If the move is valid, I will make the move. If the move is invalid, I will try a different move.<|im_end|>
                Trial 2:
                In this environment, I am trying to reach the goal position without falling into any holes. I should check the current position of the player before making a move. If the move is valid, I will make the move. If the move is invalid, I will try a different move.<|im_end|>
                    """,
                "answer":
                    """
                Based on the current game state and memories, the optimal action for the player to take would be to move right (action 3) to navigate around the holes and reach the goal position. Therefore, the optimal action to take now is to move right (action 3).
                    """
            },
            {
                "question":
                    """
                State description: Current Game State: The current position of the player is at row 1, column 0.
                Goal description: The goal is to navigate across the frozen lake and reach the goal position located at (3,3) without falling into any holes, which are located at (1,1), (1,3), (2,3) and (0,3).
                Action description: Your Next Move: 
                Please choose an action. The possible actions are:
                '1': Move left (Decrease the horizontal coordinate by 1)
                '2': Move down (Increase the vertical coordinate by 1)
                '3': Move right (Increase the horizontal coordinate by 1)
                '4': Move up (Decrease the vertical coordinate by 1). Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                Your memory for the task below:
                Trial 0:
                In this environment, I am trying to reach the goal position without falling into any holes. I should check the current position of the player before making a move. If the move is valid, I will make the move. If the move is invalid, I will try a different move.<|im_end|>
                Trial 1:
                In this environment, I am trying to reach the goal position without falling into any holes. I should check the current position of the player before making a move. If the move is valid, I will make the move. If the move is invalid, I will try a different move.<|im_end|>
                Trial 2:
                In this environment, I need to check the current position of the player before making a move. If the move is valid, I will make the move. If the move is invalid, I will try a different move.<|im_end|>
                    """,
                "answer":
                    """
                Based on the current game state and memories, the insights and the suggestions, the optimal action for the player to take would be to move down (action 2) to pick up the passenager. Therefore, the optimal action to take now is to move down (action 2).
                    """
            },
        ]

class EXE:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: The current position of the player is at row 2, column 0.
                Goal description: The goal is to navigate across the frozen lake and reach the goal position located at (3,3) without falling into any holes, which are located at (1,1), (1,3), (2,3) and (0,3).
                Action description: Your Next Move: 
                Please choose an action. The possible actions are:
                '1': Move left (Decrease the horizontal coordinate by 1)
                '2': Move down (Increase the vertical coordinate by 1)
                '3': Move right (Increase the horizontal coordinate by 1)
                '4': Move up (Decrease the vertical coordinate by 1). Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                The insights of the game are listed below: The key information that can be exploited to improve the performance of the player includes the fact that the current policy is random and ineffective, the player is not learning from its experiences, and the slippery nature of the frozen lake is causing unintended movements. To improve performance, the player needs to incorporate a learning algorithm to improve its policy over time and develop a strategy that takes into account the slippery nature of the ice.
                The suggestions are listed below:Suggestion for the next episode:
                1. Exploration: The player should explore the environment to understand the slippery nature of the frozen lake. The player can do this by taking random actions and observing the resulting movements. This will help the player to develop a better understanding of the environment and adjust its actions accordingly.
                2. Exploitation: The player should use a Q-learning algorithm to improve its policy. The Q-learning algorithm will help the player to learn from its experiences and develop a better policy over time. The player should also consider the slippery nature of the frozen lake when updating its Q-values.
                3. Weighting: The player should balance exploration and exploitation by using an epsilon-greedy policy. The player should set a high value of epsilon initially to encourage exploration and gradually decrease it over time to encourage exploitation. This will help the player to explore the environment initially and then exploit its knowledge to gain a higher performance.
                    """,
                "answer":
                    """
                Based on the current game state, the insights and the suggestions, the optimal action for the player to take would be to move right (action 3) to navigate around the holes and reach the goal position. Therefore, the optimal action to take now is to move right (action 3).
                    """
            },
        ]
