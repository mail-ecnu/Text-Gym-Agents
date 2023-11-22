class ACT:
    def __init__(self,):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
            State description: Current Game State: Taxi is at Row 4, Col 0. The passenger is at the Green location. The passenger wants to go to the Red location.
            Goal description: The goal is to navigate the taxi to the passenger, pick them up, and drop them off at their destination as efficiently as possible.
            Action description: Your Next Move: Please choose an action. Type '1' to move south (down), '2' to move north (up), '3' to move east (right), '4' to move west (left), '5' to pick up the passenger or '6' to drop off the passenger. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6].
            """,
                "answer":
                    """
            So the final answer is: move north (up) (Action 2).
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
            So the final answer is: move south (down) (Action 1).
            """
            }
        ]


class COT:
    def __init__(self,):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
            State description: Current Game State: Taxi is at Row 4, Col 0. The passenger is at the Green location. The passenger wants to go to the Red location.
            Goal description: The goal is to navigate the taxi to the passenger, pick them up, and drop them off at their destination as efficiently as possible.
            Action description: Your Next Move: Please choose an action. Type '1' to move south (down), '2' to move north (up), '3' to move east (right), '4' to move west (left), '5' to pick up the passenger or '6' to drop off the passenger. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6].
            """,
                "answer":
                    """
            The taxi is currently located at (4,0), while the passenger is located the Green location with coordinates (0,4), and their destination is the Red location at coordinates (0,0). 
            As the taxi has not yet picked up the passenger, its current task is to reach the passenger as soon as possible. 
            Given that there are walls to the east, west, and south of the taxi, the optimal action for the taxi to take in its current state is to move north.
            So the final answer is: move north (up) (Action 2).
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
            The taxi is currently located at (1,2), while the passenger is located the Yellow location with coordinates (4,0), and their destination is the Red location at coordinates (0,0). 
            As the taxi has not yet picked up the passenger, its current task is to reach the passenger as soon as possible. 
            Given that there are walls to the west of the taxi, the optimal action for the taxi to take in its current state is to move south.
            So the final answer is: move south (down) (Action 1).
            """
            }
        ]


class PAL:
    def __init__(self) -> None:
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [{
                "question":
                    """
            State description: Current Game State: Taxi is at Row 4, Col 0. The passenger is at the Green location. The passenger wants to go to the Red location.
            Goal description: The goal is to navigate the taxi to the passenger, pick them up, and drop them off at their destination as efficiently as possible.
            Action description: Your Next Move: Please choose an action. Type '1' to move south (down), '2' to move north (up), '3' to move east (right), '4' to move west (left), '5' to pick up the passenger or '6' to drop off the passenger. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6].
            """,
                "answer":
                    """
            from collections import deque

            def bfs_find_best_action(taxi_position, target_position, walls):
                queue = deque([(taxi_position, [])])
                visited = set()

                while queue:
                    current_position, path = queue.popleft()

                    if current_position == target_position:
                        if path:
                            return path[0]
                        return None

                    if current_position in visited:
                        continue

                    visited.add(current_position)
                    wall = walls.get(current_position, [])

                    for i, next_action in enumerate([(1, 0), (-1, 0), (0, 1), (0, -1)]):
                        i += 1
                        if i in wall:
                            continue

                        next_position = cal_next_position(current_position, next_action)
                        new_path = path + [i]
                        queue.append((next_position, new_path))

            def cal_dist(p1,p2):
                return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

            def cal_next_position(p,a):
                return (p[0]+a[0],p[1]+a[1])

            taxi_position = (4,0)
            passenger_position = (0,4) # the Green location
            destination = (0,0) # the Red location
            walls = dict([
                ((0, 0), [2, 4]),
                ((0, 1), [2, 3]),
                ((0, 2), [2, 4]),
                ((0, 3), [2]),
                ((0, 4), [2, 3]),
                ((1, 0), [4]),
                ((1, 1), [3]),
                ((1, 2), [4]),
                ((1, 4), [3]),
                ((2, 0), [4]),
                ((2, 4), [3]),
                ((3, 0), [3, 4]),
                ((3, 1), [4]),
                ((3, 2), [3]),
                ((3, 3), [4]),
                ((3, 4), [3]),
                ((4, 0), [1, 3, 4]),
                ((4, 1), [1, 4]),
                ((4, 2), [1, 3]),
                ((4, 3), [1, 4]),
                ((4, 4), [1, 3]),
            ])

            picked_up_flag = False
            valid_actions = [1, 2, 3, 4, 5, 6]
            action = [(1,0),(-1,0),(0,1),(0,-1)]
            action_description = dict(zip(range(1, 7), [
                "Move south (down)",
                "Move north (up)",
                "Move east (right)",
                "Move west (left)",
                "Pick up the passenger",
                "Drop off the passenger",
            ]))

            if picked_up_flag:
                if taxi_position == destination:
                    action = 6
                else:
                    action = bfs_find_best_action(taxi_position,destination,walls)
            else:
                if taxi_position == passenger_position:
                    action = 5
                    picked_up_flag = True
                else:
                    action = bfs_find_best_action(taxi_position,passenger_position,walls)
            print("The optimal action is : "+str(action_description[action])+"(Action "+str(action)+")")   
            The optimal action is : Move north (up)(Action 2).
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

                def bfs_find_best_action(taxi_position, target_position, walls):
                    queue = deque([(taxi_position, [])])
                    visited = set()

                    while queue:
                        current_position, path = queue.popleft()

                        if current_position == target_position:
                            if path:
                                return path[0]
                            return None

                        if current_position in visited:
                            continue

                        visited.add(current_position)
                        wall = walls.get(current_position, [])

                        for i, next_action in enumerate([(1, 0), (-1, 0), (0, 1), (0, -1)]):
                            i += 1
                            if i in wall:
                                continue

                            next_position = cal_next_position(current_position, next_action)
                            new_path = path + [i]
                            queue.append((next_position, new_path))

                def cal_dist(p1,p2):
                    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

                def cal_next_position(p,a):
                    return (p[0]+a[0],p[1]+a[1])

                taxi_position = (1,2)
                passenger_position = (4,0) # the Yellow location
                destination = (0,0) # the Red location
                walls = dict([
                    ((0, 0), [2, 4]),
                    ((0, 1), [2, 3]),
                    ((0, 2), [2, 4]),
                    ((0, 3), [2]),
                    ((0, 4), [2, 3]),
                    ((1, 0), [4]),
                    ((1, 1), [3]),
                    ((1, 2), [4]),
                    ((1, 4), [3]),
                    ((2, 0), [4]),
                    ((2, 4), [3]),
                    ((3, 0), [3, 4]),
                    ((3, 1), [4]),
                    ((3, 2), [3]),
                    ((3, 3), [4]),
                    ((3, 4), [3]),
                    ((4, 0), [1, 3, 4]),
                    ((4, 1), [1, 4]),
                    ((4, 2), [1, 3]),
                    ((4, 3), [1, 4]),
                    ((4, 4), [1, 3]),
                ])

                picked_up_flag = False
                valid_actions = [1, 2, 3, 4, 5, 6]
                action = [(1,0),(-1,0),(0,1),(0,-1)]
                action_description = dict(zip(range(1, 7), [
                    "Move south (down)",
                    "Move north (up)",
                    "Move east (right)",
                    "Move west (left)",
                    "Pick up the passenger",
                    "Drop off the passenger",
                ]))

                if picked_up_flag:
                    if taxi_position == destination:
                        action = 6
                    else:
                        action = bfs_find_best_action(taxi_position,destination,walls)
                else:
                    if taxi_position == passenger_position:
                        action = 5
                        picked_up_flag = True
                    else:
                        action = bfs_find_best_action(taxi_position,passenger_position,walls)
                print("The optimal action is : "+str(action_description[action])+"(Action "+str(action)+")")
                The optimal action is : Move south (down)(Action 1)
            """
            }]


class CONSISTENCY:
    def __init__(self) -> None:
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [{
                "question":
                    """
            State description: Current Game State: Taxi is at Row 4, Col 0. The passenger is at the Green location. The passenger wants to go to the Red location.
            Goal description: The goal is to navigate the taxi to the passenger, pick them up, and drop them off at their destination as efficiently as possible.
            Action description: Your Next Move: Please choose an action. Type '1' to move south (down), '2' to move north (up), '3' to move east (right), '4' to move west (left), '5' to pick up the passenger or '6' to drop off the passenger. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6].
            """,
                "answer":
                    """
            The taxi is currently located at (4,0), while the passenger is located the Green location with coordinates (0,4), and their destination is the Red location at coordinates (0,0). 
            As the taxi has not yet picked up the passenger, its current task is to reach the passenger as soon as possible. 
            Given that there are walls to the east, west, and south of the taxi, the optimal action for the taxi to take in its current state is to move north.
            So the final answer is: move north (up) (Action 2).
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
            The taxi is currently located at (1,2), while the passenger is located the Yellow location with coordinates (4,0), and their destination is the Red location at coordinates (0,0). 
            As the taxi has not yet picked up the passenger, its current task is to reach the passenger as soon as possible. 
            Given that there are walls to the west of the taxi, the optimal action for the taxi to take in its current state is to move south.
            So the final answer is: move south (down) (Action 1).
            """
            }]


class SELFASK:
    def __init__(self) -> None:
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [{
                "question":
                    """
            State description: Current Game State: Taxi is at Row 4, Col 0. The passenger is at the Green location. The passenger wants to go to the Red location.
            Goal description: The goal is to navigate the taxi to the passenger, pick them up, and drop them off at their destination as efficiently as possible.
            Action description: Your Next Move: Please choose an action. Type '1' to move south (down), '2' to move north (up), '3' to move east (right), '4' to move west (left), '5' to pick up the passenger or '6' to drop off the passenger. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6].
            """,
                "answer":
                    """
            Are follow up questions needed here: Yes.
            Follow up: What is the current location of the taxi?
            Intermediate answer: The current position of the taxi is Row 4 Col 0, i.e. (4,0).
            Follow up: Where is the passenger's current location?
            Intermediate answer: The passenger is now at the Green location at coordinates (0,4).
            Follow up: Has the taxi picked up the passenger?
            Intermediate answer: No.
            Follow up: Where is the passenger's destination?
            Intermediate answer: The passenger's destination is the Red location located at coordinates (0,0).
            Follow up: Are there any walls nearby the taxi?
            Intermediate answer: There is a wall to the east, west, and south of the taxi.
            Follow up: What is the task of the taxi in its current state?
            Intermediate answer: The task of the taxi in its current state is to pick up a passenger as soon as possible.
            Follow up: What is the optimal action for the taxi in its current state?
            Intermediate answer: The optimal action for the taxi is to move north(up).
            So the final answer is: move north (up) (Action 2).
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
            Are follow up questions needed here: Yes.
            Follow up: What is the current location of the taxi?
            Intermediate answer: The current position of the taxi is Row 1 Col 2, i.e. (1,2).
            Follow up: Where is the passenger's current location?
            Intermediate answer: The passenger is now at the Yellow location at coordinates (4,0).
            Follow up: Has the taxi picked up the passenger?
            Intermediate answer: No.
            Follow up: Where is the passenger's destination?
            Intermediate answer: The passenger's destination is the Red location located at coordinates (0,0).
            Follow up: Are there any walls nearby the taxi?
            Intermediate answer: There is a wall to the west of the taxi.
            Follow up: What is the task of the taxi in its current state?
            Intermediate answer: The task of the taxi in its current state is to pick up a passenger as soon as possible.
            Follow up: What is the optimal action for the taxi in its current state?
            Intermediate answer: The optimal action for the taxi is to move south (down).
            So the final answer is: move south (down) (Action 1).
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
                State description: Current Game State: Taxi is at Row 0, Col 1. The passenger is at the Green location. The passenger wants to go to the Blue location.
                Goal description: The goal is to navigate the taxi to the passenger, pick them up, and drop them off at their destination as efficiently as possible.
                Action description: Your Next Move: Please choose an action. Type '1' to move south (down), '2' to move north (up), '3' to move east (right), '4' to move west (left), '5' to pick up the passenger or '6' to drop off the passenger. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6].
                Your memory for the task below:
                Trial 0:
                I was stuck in a loop in which I continually moved the taxi back and forth between two locations instead of moving to the passenger's location. I should have moved the taxi to the passenger's location, then picked up the passenger, then moved to the passenger's desired destination, and dropped off the passenger. In the next trial, I will move the taxi to the passenger's location, then pick up the passenger, then move to the passenger's desired destination, and drop off the passenger.<|im_end|>
                Trial 1:
                In this environment, my plan was to move the taxi to the passenger's location, then pick up the passenger, then move to the passenger's desired destination, and drop off the passenger. However, I was stuck in a loop in which I continually moved the taxi back and forth between two locations instead of moving to the passenger's location. I should have moved the taxi to the passenger's location, then picked up the passenger, then moved to the passenger's desired destination, and dropped off the passenger. In the next trial, I will move the taxi to the passenger's location, then pick up the passenger, then move to the passenger's desired destination, and drop off the passenger.<|im_end|>
                Trial 2:
                In this environment, my plan is to move the taxi to the passenger's location, then pick up the passenger, then move to the passenger's desired destination, and drop off the passenger. I will not move the taxi back and forth between two locations.<|im_end|>
                    """,
                "answer":
                    """
                Based on the current game state and the memory, the optimal action for the player to take would be to move down (action 1) to navigate around the obstacles and pick up the passenager. Therefore, the optimal action to take now is to move down (Action 1).
                    """
            },
            {
                "question":
                    """
                State description: Current Game State: Taxi is at Row 4, Col 4. The passenger is at the Red location. The passenger wants to go to the Green location.
                Goal description: The goal is to navigate the taxi to the passenger, pick them up, and drop them off at their destination as efficiently as possible.
                Action description: Your Next Move: Please choose an action. Type '1' to move south (down), '2' to move north (up), '3' to move east (right), '4' to move west (left), '5' to pick up the passenger or '6' to drop off the passenger. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6].
                Your memory for the task below:
                Trial 0:
                In this environment, my plan was to move the taxi to the passenger's location, then pick up the passenger, then move to the passenger's desired destination, and drop off the passenger. However, I was stuck in a loop in which I continually moved the taxi back and forth between two locations instead of moving to the passenger's location. I should have moved the taxi to the passenger's location, then picked up the passenger, then moved to the passenger's desired destination, and dropped off the passenger. In the next trial, I will move the taxi to the passenger's location, then pick up the passenger, then move to the passenger's desired destination, and drop off the passenger.<|im_end|>
                Trial 1:
                In this environment, my plan is to move the taxi to the passenger's location, then pick up the passenger, then move to the passenger's desired destination, and drop off the passenger. I will not move the taxi back and forth between two locations.<|im_end|>
                Trial 2:
                In this environment, my plan is to move the taxi to the passenger's location, then pick up the passenger, then move to the passenger's desired destination, and drop off the passenger. I will not move the taxi back and forth between two locations.<|im_end|>
                    """,
                "answer":
                    """
                Based on the current game state and the memory, the optimal action for the player to take would be to move left (action 4) to pick up the passenager. Therefore, the optimal action to take now is to move left (action 4).
                    """
            },
        ]

class EGG:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: Taxi is at Row 0, Col 1. The passenger is at the Green location. The passenger wants to go to the Blue location.
                Goal description: The goal is to navigate the taxi to the passenger, pick them up, and drop them off at their destination as efficiently as possible.
                Action description: Your Next Move: Please choose an action. Type '1' to move south (down), '2' to move north (up), '3' to move east (right), '4' to move west (left), '5' to pick up the passenger or '6' to drop off the passenger. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6].
                The insights of the game are listed below: 
                1. The current policy is random and not using any information about the locations of the pick-up and drop-off points or the shortest path to reach them.
                2. The taxi is often stuck in a loop of repeatedly taking the same action, which could be addressed by implementing a penalty for repeating the same action multiple times in a row.
                3. The taxi often moves in the opposite direction of the passenger or destination, which could be addressed by incorporating a heuristic that encourages the taxi to move towards the passenger or destination.
                4. The performance of the current policy is very poor, as indicated by the negative rewards received in each episode.
                5. A more informed policy, such as a Q-learning algorithm, could be used to improve performance.
                The suggestions are listed below:
                1. The player should explore the environment by trying out different routes to reach the pick-up and drop-off locations. They should also try to identify any patterns in the locations of the pick-up and drop-off points, and use this information to plan their route. The exploration can be done by randomly selecting actions and observing the rewards obtained.
                2. To improve the policy, the player should use a Q-learning algorithm to learn the optimal policy. They should use the information obtained through exploration to update the Q-values for each state-action pair. The player should also incorporate a penalty for repeating the same action multiple times in a row and a heuristic that encourages the taxi to move towards the passenger or destination.
                3. The player should weight the exploration and exploitation differently by using an epsilon-greedy policy. They should set a high value of epsilon initially to encourage exploration and gradually decrease it over time to encourage exploitation. The player should also monitor the performance of the policy and adjust the exploration-exploitation trade-off accordingly.
                    """,
                "answer":
                    """
                Based on the current game state, the insights and the suggestions, the optimal action for the player to take would be to move down (action 1) to navigate around the obstacles and pick up the passenager. Therefore, the optimal action to take now is to move down (Action 1).
                    """
            },{
                "question":
                    """
                State description: Current Game State: Taxi is at Row 4, Col 4. The passenger is at the Red location. The passenger wants to go to the Green location.
                Goal description: The goal is to navigate the taxi to the passenger, pick them up, and drop them off at their destination as efficiently as possible.
                Action description: Your Next Move: Please choose an action. Type '1' to move south (down), '2' to move north (up), '3' to move east (right), '4' to move west (left), '5' to pick up the passenger or '6' to drop off the passenger. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6].
                The insights of the game are listed below: 
                1. The current policy is random and not using any information about the locations of the pick-up and drop-off points or the shortest path to reach them.
                2. The taxi is often stuck in a loop of repeating the same action multiple times in a row.
                3. The taxi often moves in the opposite direction of the passenger or destination.
                4. A more informed policy, such as a Q-learning algorithm, could be used to improve performance.
                5. Implementing a penalty for repeating the same action multiple times in a row could address the issue of being stuck in a loop.
                6. Incorporating a heuristic that encourages the taxi to move towards the passenger or destination could address the issue of moving in the opposite direction.
                The suggestions are listed below:Suggestion for the next episode:
                1. Exploration: The player should explore the shortest path to reach the pick-up and drop-off points. This can be done by using a heuristic algorithm such as A* search to find the shortest path. The player should also explore the penalty for repeating the same action multiple times in a row to avoid getting stuck in a loop.
                2. Exploitation: The player should use a Q-learning algorithm to improve the policy. The Q-learning algorithm should take into account the shortest path to reach the pick-up and drop-off points, as well as the penalty for repeating the same action multiple times in a row. The player should also incorporate a heuristic that encourages the taxi to move towards the passenger or destination.
                3. Weighting: The player should focus more on exploitation than exploration in this episode, as they have already explored the random policy in the previous episodes. The player should use the information obtained from the exploration to improve the policy and gain a higher performance. However, the player should still explore the penalty for repeating the same action multiple times in a row to avoid getting stuck in a loop.
                    """,
                "answer":
                    """
                Based on the current game state, the insights and the suggestions, the optimal action for the player to take would be to move left (action 4) to pick up the passenager. Therefore, the optimal action to take now is to move left (action 4).
                    """
            },
        ]

class EGGWithoutInsights:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: Taxi is at Row 0, Col 1. The passenger is at the Green location. The passenger wants to go to the Blue location.
                Goal description: The goal is to navigate the taxi to the passenger, pick them up, and drop them off at their destination as efficiently as possible.
                Action description: Your Next Move: Please choose an action. Type '1' to move south (down), '2' to move north (up), '3' to move east (right), '4' to move west (left), '5' to pick up the passenger or '6' to drop off the passenger. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6].
                The suggestions are listed below:
                1. The player should explore the environment by trying out different routes to reach the pick-up and drop-off locations. They should also try to identify any patterns in the locations of the pick-up and drop-off points, and use this information to plan their route. The exploration can be done by randomly selecting actions and observing the rewards obtained.
                2. To improve the policy, the player should use a Q-learning algorithm to learn the optimal policy. They should use the information obtained through exploration to update the Q-values for each state-action pair. The player should also incorporate a penalty for repeating the same action multiple times in a row and a heuristic that encourages the taxi to move towards the passenger or destination.
                3. The player should weight the exploration and exploitation differently by using an epsilon-greedy policy. They should set a high value of epsilon initially to encourage exploration and gradually decrease it over time to encourage exploitation. The player should also monitor the performance of the policy and adjust the exploration-exploitation trade-off accordingly.
                    """,
                "answer":
                    """
                Based on the current game state and the suggestions, the optimal action for the player to take would be to move down (action 1) to navigate around the obstacles and pick up the passenager. Therefore, the optimal action to take now is to move down (Action 1).
                    """
            },{
                "question":
                    """
                State description: Current Game State: Taxi is at Row 4, Col 4. The passenger is at the Red location. The passenger wants to go to the Green location.
                Goal description: The goal is to navigate the taxi to the passenger, pick them up, and drop them off at their destination as efficiently as possible.
                Action description: Your Next Move: Please choose an action. Type '1' to move south (down), '2' to move north (up), '3' to move east (right), '4' to move west (left), '5' to pick up the passenger or '6' to drop off the passenger. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6].
                The suggestions are listed below:Suggestion for the next episode:
                1. Exploration: The player should explore the shortest path to reach the pick-up and drop-off points. This can be done by using a heuristic algorithm such as A* search to find the shortest path. The player should also explore the penalty for repeating the same action multiple times in a row to avoid getting stuck in a loop.
                2. Exploitation: The player should use a Q-learning algorithm to improve the policy. The Q-learning algorithm should take into account the shortest path to reach the pick-up and drop-off points, as well as the penalty for repeating the same action multiple times in a row. The player should also incorporate a heuristic that encourages the taxi to move towards the passenger or destination.
                3. Weighting: The player should focus more on exploitation than exploration in this episode, as they have already explored the random policy in the previous episodes. The player should use the information obtained from the exploration to improve the policy and gain a higher performance. However, the player should still explore the penalty for repeating the same action multiple times in a row to avoid getting stuck in a loop.
                    """,
                "answer":
                    """
                Based on the current game state and the suggestions, the optimal action for the player to take would be to move left (action 4) to pick up the passenager. Therefore, the optimal action to take now is to move left (action 4).
                    """
            },
        ]

class EGGWithoutSuggestions:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: Taxi is at Row 0, Col 1. The passenger is at the Green location. The passenger wants to go to the Blue location.
                Goal description: The goal is to navigate the taxi to the passenger, pick them up, and drop them off at their destination as efficiently as possible.
                Action description: Your Next Move: Please choose an action. Type '1' to move south (down), '2' to move north (up), '3' to move east (right), '4' to move west (left), '5' to pick up the passenger or '6' to drop off the passenger. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6].
                The insights of the game are listed below: 
                1. The current policy is random and not using any information about the locations of the pick-up and drop-off points or the shortest path to reach them.
                2. The taxi is often stuck in a loop of repeatedly taking the same action, which could be addressed by implementing a penalty for repeating the same action multiple times in a row.
                3. The taxi often moves in the opposite direction of the passenger or destination, which could be addressed by incorporating a heuristic that encourages the taxi to move towards the passenger or destination.
                4. The performance of the current policy is very poor, as indicated by the negative rewards received in each episode.
                5. A more informed policy, such as a Q-learning algorithm, could be used to improve performance.
                    """,
                "answer":
                    """
                Based on the current game state and the insights, the optimal action for the player to take would be to move down (action 1) to navigate around the obstacles and pick up the passenager. Therefore, the optimal action to take now is to move down (Action 1).
                    """
            },{
                "question":
                    """
                State description: Current Game State: Taxi is at Row 4, Col 4. The passenger is at the Red location. The passenger wants to go to the Green location.
                Goal description: The goal is to navigate the taxi to the passenger, pick them up, and drop them off at their destination as efficiently as possible.
                Action description: Your Next Move: Please choose an action. Type '1' to move south (down), '2' to move north (up), '3' to move east (right), '4' to move west (left), '5' to pick up the passenger or '6' to drop off the passenger. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4, 5, 6].
                The insights of the game are listed below: 
                1. The current policy is random and not using any information about the locations of the pick-up and drop-off points or the shortest path to reach them.
                2. The taxi is often stuck in a loop of repeating the same action multiple times in a row.
                3. The taxi often moves in the opposite direction of the passenger or destination.
                4. A more informed policy, such as a Q-learning algorithm, could be used to improve performance.
                5. Implementing a penalty for repeating the same action multiple times in a row could address the issue of being stuck in a loop.
                6. Incorporating a heuristic that encourages the taxi to move towards the passenger or destination could address the issue of moving in the opposite direction.
                    """,
                "answer":
                    """
                Based on the current game state and the insights, the optimal action for the player to take would be to move left (action 4) to pick up the passenager. Therefore, the optimal action to take now is to move left (action 4).
                    """
            },
        ]