class ACT:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: 
                Current Game State: The player is at location [3, 0] in the grid world.
                Goal description: The goal is to navigate from the starting point to an target which locate at (3,11), avoiding the cliff, in as few steps as possible.
                Action description: Your Next Move:\nPlease choose an action. Type '1' to move up, '2' to move right, '3' to move down, or '4' to move left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                    """,
                "answer":
                    """
                The optimal action should be to go upward, i.e., action 1.
                    """
            },
            {
                "question":
                    """
                State description: 
                Current Game State: The player is at location [0, 11] in the grid world.
                Goal description: The goal is to navigate from the starting point to an target which locate at (3,11), avoiding the cliff, in as few steps as possible.
                Action description: Your Next Move:\nPlease choose an action. Type '1' to move up, '2' to move right, '3' to move down, or '4' to move left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                    """,
                "answer":
                    """
                The optimal action should be to go down, i.e., action 3.
                    """
            },
        ]


class COT:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: 
                Current Game State: The player is at location [3, 0] in the grid world.
                Goal description: The goal is to navigate from the starting point to an target which locate at (3,11), avoiding the cliff, in as few steps as possible.
                Action description: Your Next Move:\nPlease choose an action. Type '1' to move up, '2' to move right, '3' to move down, or '4' to move left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                    """,
                "answer":
                    """
                The player is now at position (3,0), with a wall to his left and a wall below him. Since (3, 1...10) is a cliff, i.e., the player's right side is a cliff, the optimal action should be to go upward, i.e., action 1.
                    """
            },
            {
                "question":
                    """
                State description: 
                Current Game State: The player is at location [0, 11] in the grid world.
                Goal description: The goal is to navigate from the starting point to an target which locate at (3,11), avoiding the cliff, in as few steps as possible.
                Action description: Your Next Move:\nPlease choose an action. Type '1' to move up, '2' to move right, '3' to move down, or '4' to move left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                    """,
                "answer":
                    """
                The player is now at position (0,11), with a wall to his right and a wall above him. Since (3, 1...10) is a cliff, i.e., there is no cliff in the player's neighborhood, and since the end point (3,11) is below the player, the optimal action should be to go down, i.e., action 3.
                    """
            },
        ]


class PAL:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: 
                Current Game State: The player is at location [3, 0] in the grid world.
                Goal description: The goal is to navigate from the starting point to an target which locate at (3,11), avoiding the cliff, in as few steps as possible.
                Action description: Your Next Move:\nPlease choose an action. Type '1' to move up, '2' to move right, '3' to move down, or '4' to move left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                    """,
                "answer":
                    """
                current_pos = (3,0)
                cliff_pos = [(3,i) for i in range(1,11)]
                action_list = [(-1,0),(0,1),(1,0),(0,-1)]
                action_dist = []
                target_pos = (3,11)
                for action in action_list:
                    if current_pos[0] + action[0] > 3 or current_pos[0] + action[0] < 0:
                        next_pos_x = current_pos[0]
                    else:
                        next_pos_x = current_pos[0] + action[0]

                    if current_pos[1] + action[1] > 11 or current_pos[1] + action[1] < 0:
                        next_pos_y = current_pos[1]
                    else:
                        next_pos_y = current_pos[1] + action[1]

                    if (next_pos_x,next_pos_y) in cliff_pos or (next_pos_x,next_pos_y) == current_pos:
                        action_dist.append(100)
                    else:
                        # target_pos[0] = 3 target_pos[1] = 11
                        distance = abs(target_pos[0]-next_pos_x) + abs(target_pos[1]-next_pos_y) # 
                        action_dist.append(distance)

                # action_dist = [12, 100, 100, 100]
                a = action_dist.index(min(action_dist))
                action = a + 1
                print("The best action is:", action)
                So the final answer is : The best action is: action 1.
                    """
            },
            {
                "question":
                    """
                State description: 
                Current Game State: The player is at location [0, 11] in the grid world.
                Goal description: The goal is to navigate from the starting point to an target which locate at (3,11), avoiding the cliff, in as few steps as possible.
                Action description: Your Next Move:\nPlease choose an action. Type '1' to move up, '2' to move right, '3' to move down, or '4' to move left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                    """,
                "answer":
                    """
                current_pos = (0,11)
                cliff_pos = [(3,i) for i in range(1,11)]
                action_list = [(-1,0),(0,1),(1,0),(0,-1)]
                action_dist = []
                target_pos = (3,11)
                for action in action_list:
                    if current_pos[0] + action[0] > 3 or current_pos[0] + action[0] < 0:
                        next_pos_x = current_pos[0]
                    else:
                        next_pos_x = current_pos[0] + action[0]

                    if current_pos[1] + action[1] > 11 or current_pos[1] + action[1] < 0:
                        next_pos_y = current_pos[1]
                    else:
                        next_pos_y = current_pos[1] + action[1]

                    if (next_pos_x,next_pos_y) in cliff_pos or (next_pos_x,next_pos_y) == current_pos:
                        action_dist.append(100)
                    else:
                        # target_pos[0] = 3 target_pos[1] = 11
                        distance = abs(target_pos[0]-next_pos_x) + abs(target_pos[1]-next_pos_y) # 
                        action_dist.append(distance)

                # action_dist = [100, 100, 3, 4]
                a = action_dist.index(min(action_dist))
                action = a + 1
                print("The best action is:", action)
                So the final answer is : The best action is: action 3.
                    """
            },
        ]


class CONSISTENCY:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: 
                Current Game State: The player is at location [3, 0] in the grid world.
                Goal description: The goal is to navigate from the starting point to an target which locate at (3,11), avoiding the cliff, in as few steps as possible.
                Action description: Your Next Move:\nPlease choose an action. Type '1' to move up, '2' to move right, '3' to move down, or '4' to move left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                    """,
                "answer":
                    """
                The player is now at position (3,0), with a wall to his left and a wall below him. Since (3, 1...10) is a cliff, i.e., the player's right side is a cliff, the optimal action should be to go upward, i.e., action 1.
                    """
            },
            {
                "question":
                    """
                State description: 
                Current Game State: The player is at location [0, 11] in the grid world.
                Goal description: The goal is to navigate from the starting point to an target which locate at (3,11), avoiding the cliff, in as few steps as possible.
                Action description: Your Next Move:\nPlease choose an action. Type '1' to move up, '2' to move right, '3' to move down, or '4' to move left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                    """,
                "answer":
                    """
                The player is now at position (0,11), with a wall to his right and a wall above him. Since (3, 1...10) is a cliff, i.e., there is no cliff in the player's neighborhood, and since the end point (3,11) is below the player, the optimal action should be to go down, i.e., action 3.
                    """
            },
        ]


class SELFASK:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: 
                Current Game State: The player is at location [3, 0] in the grid world.
                Goal description: The goal is to navigate from the starting point to an target which locate at (3,11), avoiding the cliff, in as few steps as possible.
                Action description: Your Next Move:\nPlease choose an action. Type '1' to move up, '2' to move right, '3' to move down, or '4' to move left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                    """,
                "answer":
                    """
                Are follow up questions needed here: Yes.
                Follow up: What is the player's current location?
                Intermediate answer: The player is now at position (3,0).
                Follow up: Are there walls around the players?
                Intermediate answer: Yes, there are walls below and to the left of the player.
                Follow up: Are there cliffs around the players?
                Intermediate answer: Yes, the cliff is at location (3,1-10), so there are cliffs to the right of the players.
                Follow up: Where is the location of the target point in the player's orientation?
                Intermediate answer: The target point is at position (3,11), located to the right of the player.
                Follow up: What are the actions available to the player?
                Intermediate answer: Up.
                Follow up: So what is the optimal action for the player to take in order to get to the goal point as quickly as possible??
                Intermediate answer: Up.
                So the final answer is: move up (Action 1).
                    """
            },
            {
                "question":
                    """
                State description: 
                Current Game State: The player is at location [0, 11] in the grid world.
                Goal description: The goal is to navigate from the starting point to an target which locate at (3,11), avoiding the cliff, in as few steps as possible.
                Action description: Your Next Move:\nPlease choose an action. Type '1' to move up, '2' to move right, '3' to move down, or '4' to move left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                    """,
                "answer":
                    """
                Are follow up questions needed here: Yes.
                Follow up: What is the player's current location?
                Intermediate answer: The player is now at position (0,11).
                Follow up: Are there walls around the players?
                Intermediate answer: Yes, there are walls to the right and above the players.
                Follow up: Are there cliffs around the players?
                Intermediate answer: No, the cliff is at location (3,1-10), so there is no cliff near the player.
                Follow up: Where is the location of the target point in the player's orientation?
                Intermediate answer: The location of the target point is (3,11), so below the player.
                Follow up: What are the actions available to the player?
                Intermediate answer: Down or Left.
                Follow up: So what is the optimal action for the player to take in order to get to the goal point as quickly as possible??
                Intermediate answer: Down.
                So the final answer is: move down (Action 3).
                    """
            },
        ]


class SPP:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
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
            }
]

class REFLEXION:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: The player is at location [2, 11] in the grid world.
                Goal description: The goal is to navigate from the starting point to an target which locate at (3,11), avoiding the cliff, in as few steps as possible.
                Action description: Your Next Move:\nPlease choose an action. Type '1' to move up, '2' to move right, '3' to move down, or '4' to move left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                Your memory for the task below:
                Trial 0:
                I was stuck in a loop in which I continually executed the same action instead of finding the correct path. I should have thought about the correct path to the goal location and executed the actions that lead to the goal. In the next trial, I will think about the correct path to the goal location and execute the actions that lead to the goal.<|im_end|>
                Trial 1:
                I will think about the correct path to the goal location and execute the actions that lead to the goal. The correct path is to move right until the edge of the cliff, then move up until the goal location. In the next trial, I will move right until the edge of the cliff, then move up until the goal location.<|im_end|>
                Trial 2:
                In this environment, my plan was to move randomly instead of finding the correct path to the goal location. I should have thought about the correct path to the goal location and executed the actions that lead to the goal. In the next trial, I will think about the correct path to the goal location and execute the actions that lead to the goal. The correct path is to move right until the edge of the cliff, then move up until the goal location.<|im_end|>
                    """,
                "answer":
                    """
                Based on the previous trials, the correct path to the goal location is to move up until the edge of the cliff, then move right or move down until the goal location. Therefore, the optimal action to take now is to move down (Action 3).
                    """
            },
            {
                "question":
                    """
                State description: Current Game State: The player is at location [3,0] in the grid world.
                Goal description: The goal is to navigate from the starting point to an target which locate at (3,11), avoiding the cliff, in as few steps as possible.
                Action description: Your Next Move:\nPlease choose an action. Type '1' to move up, '2' to move right, '3' to move down, or '4' to move left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                Your memory for the task below:
                Trial 0:
                I will think about the correct path to the goal location and execute the actions that lead to the goal. The correct path is to move right until the edge of the cliff, then move up until the goal location. In the next trial, I will move right until the edge of the cliff, then move up until the goal location.<|im_end|>
                Trial 1:
                In this environment, my plan was to move randomly instead of finding the correct path to the goal location. I should have thought about the correct path to the goal location and executed the actions that lead to the goal. In the next trial, I will think about the correct path to the goal location and execute the actions that lead to the goal. The correct path is to move right until the edge of the cliff, then move up until the goal location.<|im_end|>
                Trial 2:
                In the next trial, I will think about the correct path to the goal location and execute the actions that lead to the goal. The correct path is to move right until the edge of the cliff, then move up until the goal location.<|im_end|>
                    """,
                "answer":
                    """
                Based on the previous trials, the correct path to the goal location is to move up until the edge of the cliff, then move right or move down until the goal location. Therefore, the optimal action to take now is to move up (Action 1).
                    """
            },
        ]

class EXE:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: The player is at location [2, 11] in the grid world.
                Goal description: The goal is to navigate from the starting point to an target which locate at (3,11), avoiding the cliff, in as few steps as possible.
                Action description: Your Next Move:\nPlease choose an action. Type '1' to move up, '2' to move right, '3' to move down, or '4' to move left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                The insights of the game are listed below: The key information that can be exploited to improve the player's performance is that they tend to move in a straight line towards the goal location, even if it means getting closer to the cliff. This behavior can be addressed by incorporating a more cautious approach that prioritizes avoiding the cliff over reaching the goal quickly. Additionally, the policy could be updated to encourage exploration of different paths towards the goal location, rather than always moving in a straight line. The negative consequences of not prioritizing cliff avoidance are highlighted in the player's poor performance and multiple penalties.
                The suggestions are listed below:Suggestion for the next episode:
                1. Exploration: The player should explore different paths towards the goal location, rather than always moving in a straight line. This can be done by randomly selecting actions with a certain probability, such as 10%, to encourage the player to try different paths. The player should also try to gather information about the rewards and penalties associated with different actions, especially those near the cliff.
                2. Exploitation: The player should prioritize avoiding the cliff over reaching the goal quickly. This can be done by updating the policy to include a penalty for moving towards the cliff or a reward for moving away from it. The player should also try to incorporate a more cautious approach that considers the potential consequences of each action.
                3. Weighting: The player should balance exploration and exploitation by assigning a higher weight to exploitation. This is because the player has already tried two episodes and needs to focus on improving performance. However, some level of exploration is still necessary to avoid getting stuck in a suboptimal policy. A reasonable weighting could be 70% exploitation and 30% exploration.
                    """,
                "answer":
                    """
                Based on the current game state, the insights and the suggestions, the optimal action for the player to take would be to move down (action 3) to reach the goal location at [3, 11]. Therefore, the optimal action to take now is to move down (Action 3).
                    """
            },{
                "question":
                    """
                State description: Current Game State: The player is at location [3,0] in the grid world.
                Goal description: The goal is to navigate from the starting point to an target which locate at (3,11), avoiding the cliff, in as few steps as possible.
                Action description: Your Next Move:\nPlease choose an action. Type '1' to move up, '2' to move right, '3' to move down, or '4' to move left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                The insights of the game are listed below: The key information that can be exploited to improve performance of the player is that they tend to move in a straight line or zigzag pattern towards the goal location, even if it means getting closer to the cliff. This behavior can be improved by incorporating a more cautious approach that prioritizes avoiding the cliff over reaching the goal quickly, and by encouraging exploration of different paths towards the goal location. Additionally, the policy could be updated to include a penalty for falling off the cliff, which would further incentivize the player to avoid it.
                The suggestions are listed below:
                1. The player should explore different paths towards the goal location, especially those that are not in a straight line or zigzag pattern. This can be done by randomly selecting actions or by using a more exploratory policy, such as epsilon-greedy or softmax. The player should also pay attention to the rewards and penalties associated with each action, especially those related to cliff avoidance.
                2. To improve performance, the policy should prioritize both reaching the goal location and avoiding the cliff. This can be done by incorporating a penalty for moving towards the cliff or a reward for moving away from it. The policy should also encourage diagonal movements towards the goal location, which would reduce the number of steps needed to reach the goal. Additionally, the policy should include a penalty for falling off the cliff, which would further incentivize the player to avoid it.
                3. The player should balance exploration and exploitation by using a more exploratory policy, such as epsilon-greedy or softmax, with a low exploration rate. This would allow the player to explore different paths towards the goal location while still prioritizing cliff avoidance and efficient movements. The player should also periodically evaluate the policy and adjust the exploration rate accordingly.

                    """,
                "answer":
                    """
                Based on the current game state, it seems like the player is stuck in a loop and not making any progress towards the goal location. 
                To improve performance, the player should prioritize both reaching the goal location and avoiding the cliff. 
                It is recommended to incorporate a penalty for moving towards the cliff or a reward for moving away from it. 
                The policy should also encourage diagonal movements towards the goal location, which would reduce the number of steps needed to reach the goal. 
                For the next action, I suggest the player to move up (action 1) to explore a different path towards the goal location. 
                    """
            },
        ]

