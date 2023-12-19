class ACT:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: The car is positioned at -0.566, with a velocity of 0.000 towards the left.
                Goal description: The goal is to reach the flag placed on top of the right hill as quickly as possible.
                Action description: Your Next Move: Please select a numerical value within the range of [-1,1], which represents the directional force being applied to the car. The action will be limited to the range of [-1,1], and then multiplied by a power of 0.0015..
                    """,
                "answer":
                    """So the final answer is: Action 1.0."""
            },
            {
                "question":
                    """
                State description: Current Game State: The car is positioned at -0.389, with a velocity of 0.003 towards the right.
                Goal description: The goal is to reach the flag placed on top of the right hill as quickly as possible.
                Action description: Your Next Move: Please select a numerical value within the range of [-1,1], which represents the directional force being applied to the car. The action will be limited to the range of [-1,1], and then multiplied by a power of 0.0015..
                    """,
                "answer":
                    """
                So the final answer is: Action 1.0.
                    """
            },
        ]


class COT:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: The car is positioned at -0.566, with a velocity of 0.000 towards the left.
                Goal description: The goal is to reach the flag placed on top of the right hill as quickly as possible.
                Action description: Your Next Move: Please select a numerical value within the range of [-1,1], which represents the directional force being applied to the car. The action will be limited to the range of [-1,1], and then multiplied by a power of 0.0015..
                    """,
                "answer":
                    """In the specific case where the car is positioned at -0.566 with a velocity of 0.000 towards the left, the goal is to reach the flag placed on top of the right hill as quickly as possible.
                    Since the car is positioned on the left side of the environment and has a zero velocity towards the left, the car should accelerate to the right in order to move towards the goal position.
                    Accelerating to the right will help the car gain more momentum and potentially climb the hill faster.
                    So the final answer is: Action 1.0."""
            },
            {
                "question":
                    """
                State description: Current Game State: The car is positioned at -0.389, with a velocity of 0.003 towards the right.
                Goal description: The goal is to reach the flag placed on top of the right hill as quickly as possible.
                Action description: Your Next Move: Please select a numerical value within the range of [-1,1], which represents the directional force being applied to the car. The action will be limited to the range of [-1,1], and then multiplied by a power of 0.0015..
                    """,
                "answer":
                    """
                In the specific case where the car is positioned at -0.389, with a velocity of 0.003 towards the right, the goal is to reach the flag placed on top of the right hill as quickly as possible.
                Since the car is positioned on the left side of the environment and has a positive velocity pointing towards the right, the optimal action would be to accelerate to the right.
                Accelerating to the right will help the car gain more momentum and potentially climb the hill faster.
                So the final answer is: Action 1.0.
                    """
            },
        ]


class PAL:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State:  The car is positioned at -0.433, with a velocity of 0.000 towards the left.
                Goal description: The goal is to reach the flag placed on top of the right hill as quickly as possible.
                Action description: Your Next Move: Please select a numerical value within the range of [-1,1], which represents the directional force being applied to the car. The action will be limited to the range of [-1,1], and then multiplied by a power of 0.0015.
                    """,
                "answer":
                    """
                    ```python
                    current_position = -0.433
                    current_velocity = 0.000
                    if current_position < 0:
                        if current_position < -0.35:
                            if abs(current_velocity) < 0.3:
                                action = 1.0
                            else:
                                action = 0.5
                        else:
                            if abs(current_velocity) > 0.2:
                                action = -1.0
                            else:
                                action = 0.8
                    # If the car is to the right of the flag, then it needs a negative force to slow down and stop near the flag.
                    else:
                        if current_position > 0.55:
                            if abs(current_velocity) > 0.2:
                                action = -1.0
                            else:
                                action = -0.5
                        else:
                            if abs(current_velocity) < 0.2:
                                action = 0.8
                            else:
                                action = -0.5
                    print("The final answer is action", action)
                    ```
                    So The final answer is action 1.0.
                    """
            },
            {
                "question":
                    """
                State description: Current Game State:  The car is positioned at -0.189, with a velocity of 0.005 towards the right.
                Goal description: The goal is to reach the flag placed on top of the right hill as quickly as possible.
                Action description: Your Next Move: Please select a numerical value within the range of [-1,1], which represents the directional force being applied to the car. The action will be limited to the range of [-1,1], and then multiplied by a power of 0.0015.
                    """,
                "answer":
                    """
                    ```python
                    current_position = -0.189
                    current_velocity = 0.005
                    if current_position < 0:
                        if current_position < -0.35:
                            if abs(current_velocity) < 0.3:
                                action = 1.0
                            else:
                                action = 0.5
                        else:
                            if abs(current_velocity) > 0.2:
                                action = -1.0
                            else:
                                action = 0.8
                    # If the car is to the right of the flag, then it needs a negative force to slow down and stop near the flag.
                    else:
                        if current_position > 0.55:
                            if abs(current_velocity) > 0.2:
                                action = -1.0
                            else:
                                action = -0.5
                        else:
                            if abs(current_velocity) < 0.2:
                                action = 0.8
                            else:
                                action = -0.5
                    print("The final answer is action", action)
                    ```
                    So The final answer is action 0.8.
                    """
            },
        ]


class CONSISTENCY:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: The car is positioned at -0.566, with a velocity of 0.000 towards the left.
                Goal description: The goal is to reach the flag placed on top of the right hill as quickly as possible.
                Action description: Your Next Move: Please select a numerical value within the range of [-1,1], which represents the directional force being applied to the car. The action will be limited to the range of [-1,1], and then multiplied by a power of 0.0015..
                    """,
                "answer":
                    """In the specific case where the car is positioned at -0.566 with a velocity of 0.000 towards the left, the goal is to reach the flag placed on top of the right hill as quickly as possible.
                    Since the car is positioned on the left side of the environment and has a zero velocity towards the left, the car should accelerate to the right in order to move towards the goal position.
                    Accelerating to the right will help the car gain more momentum and potentially climb the hill faster.
                    So the final answer is: Action 1.0."""
            },
            {
                "question":
                    """
                State description: Current Game State: The car is positioned at -0.389, with a velocity of 0.003 towards the right.
                Goal description: The goal is to reach the flag placed on top of the right hill as quickly as possible.
                Action description: Your Next Move: Please select a numerical value within the range of [-1,1], which represents the directional force being applied to the car. The action will be limited to the range of [-1,1], and then multiplied by a power of 0.0015..
                    """,
                "answer":
                    """
                In the specific case where the car is positioned at -0.389, with a velocity of 0.003 towards the right, the goal is to reach the flag placed on top of the right hill as quickly as possible.
                Since the car is positioned on the left side of the environment and has a positive velocity pointing towards the right, the optimal action would be to accelerate to the right.
                Accelerating to the right will help the car gain more momentum and potentially climb the hill faster.
                So the final answer is: Action 1.0.
                    """
            },
        ]


class SELFASK:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: The car is positioned at -0.566, with a velocity of 0.000 towards the left.
                Goal description: The goal is to reach the flag placed on top of the right hill as quickly as possible.
                Action description: Your Next Move: Please select a numerical value within the range of [-1,1], which represents the directional force being applied to the car. The action will be limited to the range of [-1,1], and then multiplied by a power of 0.0015..
                    """,
                "answer":
                    """
                Are follow up questions needed here: Yes.
                Follow up: What is the current position of the car?
                Intermediate answer: The current position of the car is -0.566.
                Follow up: What is the current velocity of the car?
                Intermediate answer: The current velocity of the car is 0.000, pointing towards the left.
                Follow up: What is the goal position?
                Intermediate answer: The goal position is to reach the flag on top of the right hill.
                Follow up: Considering the car's current position and velocity, what should be its next action?
                Intermediate answer: Since the car is positioned on the left side of the environment and its goal is to go to the right, the optimal action would be to accelerate to the right.
                So the final answer is: Action 1.0.
                    """
            },
            {
                "question":
                    """
                State description: Current Game State: The car is positioned at -0.389, with a velocity of 0.003 towards the right.
                Goal description: The goal is to reach the flag placed on top of the right hill as quickly as possible.
                Action description: Your Next Move: Please select a numerical value within the range of [-1,1], which represents the directional force being applied to the car. The action will be limited to the range of [-1,1], and then multiplied by a power of 0.0015..
                    """,
                "answer":
                    """
                Are follow up questions needed here: Yes.
                Follow up: What is the current position of the car?
                Intermediate answer: The current position of the car is -0.389.
                Follow up: What is the current velocity of the car?
                Intermediate answer: The current velocity of the car is 0.003, pointing towards the right.
                Follow up: What is the goal position?
                Intermediate answer: The goal position is to reach the flag on top of the right hill.
                Follow up: Considering the car's current position and velocity, what should be its next action?
                Intermediate answer: Since the car is positioned on the left side of the environment and its goal is to go to the right, with a velocity of 0.003 towards the right, the optimal action would be to accelerate to the right. This will help the car gain more momentum and potentially climb the hill faster.
                So the final answer is: Action 1.0.
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
                State description: Current Game State: The car is positioned at 0.472, with a velocity of 0.049 towards the right.
                Goal description: The goal is to reach the flag placed on top of the right hill as quickly as possible.
                Action description: Your Next Move: Please select a numerical value within the range of [-1,1], which represents the directional force being applied to the car. The action will be limited to the range of [-1,1], and then multiplied by a power of 0.0015..
                Your memory for the task below:
                Trial 0:
                In this environment, my plan was to accelerate the car to the right as quickly as possible. However, the goal of the game is to reach the flag placed on top of the right hill as quickly as possible. I should have accelerated the car to the right until it had enough velocity to reach the top of the left hill, then I should have accelerated the car to the left to reach the flag. In the next trial, I will accelerate the car to the right until it has enough velocity to reach the top of the left hill, then I will accelerate the car to the left to reach the flag.<|im_end|>
                Trial 1:
                I will accelerate the car to the right until it has enough velocity to reach the top of the left hill, then I will accelerate the car to the left to reach the flag.<|im_end|>
                Trial 2:
                In this environment, my plan was to accelerate the car to the right until it had enough velocity to reach the top of the left hill, then I should have accelerated the car to the left to reach the flag. However, I did not take into account the fact that the car may not have enough velocity to reach the top of the left hill. I should have monitored the car's velocity and adjusted my strategy accordingly. In the next trial, I will accelerate the car to the right until it has enough velocity to reach the top of the left hill, then I will monitor the car's velocity and adjust my strategy accordingly.<|im_end|>
                    """,
                "answer":
                    """
                Based on the current game state and memories of the task, the optimal action for the player to take would be to accelerate to the right (Action 1.0). Therefore, the optimal action to take now is to push the cart to accelerate to the right (Action 1.0).
                    """
            },
            {
                "question":
                    """
                State description: Current Game State: The car is positioned at -0.218, with a velocity of 0.002 towards the left.
                Goal description: The goal is to reach the flag placed on top of the right hill as quickly as possible.
                Action description: Your Next Move: Please select a numerical value within the range of [-1,1], which represents the directional force being applied to the car. The action will be limited to the range of [-1,1], and then multiplied by a power of 0.0015..
                Your memory for the task below:
                Trial 0:
                I will accelerate the car to the right until it has enough velocity to reach the top of the left hill, then I will accelerate the car to the left to reach the flag.<|im_end|>
                Trial 1:
                In this environment, my plan was to accelerate the car to the right until it had enough velocity to reach the top of the left hill, then I should have accelerated the car to the left to reach the flag. However, I did not take into account the fact that the car may not have enough velocity to reach the top of the left hill. I should have monitored the car's velocity and adjusted my strategy accordingly. In the next trial, I will accelerate the car to the right until it has enough velocity to reach the top of the left hill, then I will monitor the car's velocity and adjust my strategy accordingly.<|im_end|>
                Trial 2:
                I will accelerate the car to the right until it has enough velocity to reach the top of the left hill, then I will monitor the car's velocity and adjust my strategy accordingly. If the car has enough velocity, I will accelerate the car to the left to reach the flag. If the car does not have enough velocity, I will continue to accelerate the car to the right until it does.<|im_end|>
                    """,
                "answer":
                    """
                Based on the current game state and memories of the task, the optimal action for the player to take would be to accelerate to the left (Action -1.0) to obtain potential energy of rightward motion. Therefore, the optimal action to take now is to accelerate to the left (Action -1.0).
                    """
            },
        ]

class EXE:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: The car is positioned at 0.472, with a velocity of 0.049 towards the right.
                Goal description: The goal is to reach the flag placed on top of the right hill as quickly as possible.
                Action description: Your Next Move: Please select a numerical value within the range of [-1,1], which represents the directional force being applied to the car. The action will be limited to the range of [-1,1], and then multiplied by a power of 0.0015..
                The insights of the game are listed below: The key information that can be exploited to improve performance of the player includes the fact that the car often gets stuck in local minima, the policy of constantly accelerating in the direction of the goal with occasional changes in direction, and the use of exploration techniques to encourage the car to try out different actions and explore the environment more thoroughly. Additionally, a more sophisticated memory system that takes into account the car's velocity and position, rather than just its position, and a different algorithm that balances exploration and exploitation more effectively can also improve performance.
                The suggestions are listed below:Suggestion for the next episode:
                1. Exploration: In the next episode, the player should focus on exploring the environment more thoroughly by trying out different actions. Specifically, the player should try accelerating in both directions (left and right) to see if there are any hidden paths that can lead to the goal state more quickly. To encourage exploration, the player can add some randomness to the policy by choosing actions randomly with a certain probability (e.g., 10% of the time).
                2. Exploitation: To improve performance, the player should continue to use the policy that has been successful in the past episodes, which is to constantly accelerate in the direction of the goal, with occasional changes in direction to avoid getting stuck in local minima. However, the player should also try to optimize the policy by adjusting the frequency of changes in direction based on the car's velocity and position. For example, if the car is moving slowly and is far from the goal, the player should consider changing direction more frequently to explore more of the environment.
                3. Exploration vs. Exploitation: The player should balance exploration and exploitation by adjusting the probability of choosing actions randomly. In the beginning of the episode, the player should focus more on exploration by choosing actions randomly with a higher probability
                    """,
                "answer":
                    """
                Based on the current game state, the insights and the suggestions, the optimal action for the player to take would be to accelerate to the right (Action 1.0). Therefore, the optimal action to take now is to push the cart to accelerate to the right (Action 1.0).
                    """
            },{
                "question":
                    """
                State description: Current Game State: The car is positioned at -0.218, with a velocity of 0.002 towards the left.
                Goal description: The goal is to reach the flag placed on top of the right hill as quickly as possible.
                Action description: Your Next Move: Please select a numerical value within the range of [-1,1], which represents the directional force being applied to the car. The action will be limited to the range of [-1,1], and then multiplied by a power of 0.0015..
                The insights of the game are listed below: 
                1. The policy of constantly accelerating towards the goal with occasional changes in direction to avoid local minima is not performing well.
                2. Exploration techniques can be used to encourage the car to try out different actions and explore the environment more thoroughly.
                3. A more sophisticated memory system that takes into account the car's velocity and position can improve the accuracy of the value function.
                4. A different algorithm that balances exploration and exploitation more effectively can also be considered.
                5. The car is able to gain enough momentum to climb the hill towards the goal, but still gets stuck in local minima at times.
                The suggestions are listed below:
                1. The player should explore different acceleration strategies, such as accelerating in the opposite direction of the goal or accelerating randomly, to gather information on the environment and avoid getting stuck in local minima. This can be done by adding some randomness to the policy or using a different algorithm that balances exploration and exploitation.
                2. To improve policy performance, the player can use the information gathered from exploration to update the value function and adjust the policy accordingly. Additionally, the player can consider using a more sophisticated memory system that takes into account the car's velocity and position, rather than just its position, to better capture the dynamics of the environment.
                3. The player should balance exploration and exploitation by allocating a certain percentage of actions to exploration and the remaining percentage to exploitation. This can be done by setting a threshold for the amount of exploration and adjusting it based on the performance of the policy. The player should also monitor the performance of the policy and adjust the balance between exploration and exploitation accordingly.
                    """,
                "answer":
                    """
                Based on the current game state, the insights and the suggestions, the optimal action for the player to take would be to accelerate to the left (Action -1.0) to obtain potential energy of rightward motion. Therefore, the optimal action to take now is to accelerate to the left (Action -1.0).
                    """
            },
        ]
