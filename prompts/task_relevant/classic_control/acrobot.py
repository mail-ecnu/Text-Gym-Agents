class ACT:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: Link1: angle theta1 0.02 radians, rotating 0.01 radians per second counterclockwise. Link2: angle theta2 -0.05 radians relative to Link1, rotating 0.02 radians per second counterclockwise.
                Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0.
                Action description: Your Next Move: \n Please choose an action. Type '1' to apply -1 torque, '2' to apply 0 torque, or '3' to apply 1 torque. Ensure you provide the action number from the valid action list, i.e., [1, 2, 3].
                    """,
                "answer":
                    """
                So the final answer is: apply 1 torque (Action 3).
                    """
            },
            {
                "question":
                    """
                State description: Current Game State: Link1: angle theta1 -0.01 radians, rotating 0.27 radians per second counterclockwise. Link2: angle theta2 -0.01 radians relative to Link1, rotating 0.61 radians per second clockwise.
                Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0
                Action description: Valid action list: [1, 2, 3]. Action 1 means to apply -1 torque, Action 2 means apply 0 torque, and Action 3 means apply 1 torque.
                    """,
                "answer":
                    """
                So the final answer is: apply -1 torque (Action 1).
                    """
            }
        ]


class PAL:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: Link1: angle theta1 0.02 radians, rotating 0.01 radians per second counterclockwise. Link2: angle theta2 -0.05 radians relative to Link1, rotating 0.02 radians per second counterclockwise.
                Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0.
                Action description: Your Next Move: \n Please choose an action. Type '1' to apply -1 torque, '2' to apply 0 torque, or '3' to apply 1 torque. Ensure you provide the action number from the valid action list, i.e., [1, 2, 3].
                    """,
                "answer":
                    """
                theta1 = 0.02
                theta2 = -0.05
                omega1 = -0.01
                omega2 = -0.02
                action_list = [-1, 0, 1]
                target_height = 1.0
                current_height = -cos(theta1) - cos(theta2 + theta1)

                action_effects = []
                # Evaluate the effects of each action on getting closer to the target height
                for action in action_list:
                    torque_effect = omega1 * (action * -1) + omega2 * (action * 1)
                    new_height = current_height + torque_effect
                    action_effects.append(new_height - target_height)

                # Choose the action that gets us closest to the target height
                best_action_index = action_effects.index(min(action_effects, key=abs))
                best_action = action_list[best_action_index]
                print("The best action is: action ", best_action_index+1)
                So the final answer is: The best action is: action 1.
                    """
            },
            {
                "question":
                    """
                State description: Current Game State: Link1: angle theta1 -0.01 radians, rotating 0.27 radians per second counterclockwise. Link2: angle theta2 -0.01 radians relative to Link1, rotating 0.61 radians per second clockwise.
                Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0
                Action description: Valid action list: [1, 2, 3]. Action 1 means to apply -1 torque, Action 2 means apply 0 torque, and Action 3 means apply 1 torque.
                    """,
                "answer":
                    """
                theta1 = -0.01
                theta2 = -0.01
                omega1 = -0.27
                omega2 = 0.61
                action_list = [-1, 0, 1]
                target_height = 1.0
                current_height = -cos(theta1) - cos(theta2 + theta1)

                action_effects = []
                # Evaluate the effects of each action on getting closer to the target height
                for action in action_list:
                    torque_effect = omega1 * (action * -1) + omega2 * (action * 1)
                    new_height = current_height + torque_effect
                    action_effects.append(new_height - target_height)

                # Choose the action that gets us closest to the target height
                best_action_index = action_effects.index(min(action_effects, key=abs))
                best_action = action_list[best_action_index]

                print("The best action is: action ", best_action_index+1)
                So the final answer is: The best action is: action 2.
                    """
            }
        ]


class COT:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: Link1: angle theta1 0.02 radians, rotating 0.01 radians per second counterclockwise. Link2: angle theta2 -0.05 radians relative to Link1, rotating 0.02 radians per second counterclockwise.
                Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0.
                Action description: Your Next Move: \n Please choose an action. Type '1' to apply -1 torque, '2' to apply 0 torque, or '3' to apply 1 torque. Ensure you provide the action number from the valid action list, i.e., [1, 2, 3].
                    """,
                "answer":
                    """
                In the current state, Link1 has an angle of 0.02 radians and is rotating counterclockwise at 0.01 radians per second. 
                Meanwhile, Link2 has an angle of -0.05 radians relative to Link1 and is also rotating counterclockwise at 0.02 radians per second. 
                The goal is to swing the free end above the target height by applying torque on the actuator.
                Given the current state, applying a positive torque (Action 3) will accelerate the counterclockwise rotation of both Link1 and Link2. 
                This will help swing the free end upward, potentially bringing it closer to the target height and improving the chances of achieving the goal.
                So the final answer is: apply 1 torque (Action 3).
                    """
            },
            {
                "question":
                    """
                State description: Current Game State: Link1: angle theta1 -0.01 radians, rotating 0.27 radians per second counterclockwise. Link2: angle theta2 -0.01 radians relative to Link1, rotating 0.61 radians per second clockwise.
                Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0
                Action description: Valid action list: [1, 2, 3]. Action 1 means to apply -1 torque, Action 2 means apply 0 torque, and Action 3 means apply 1 torque.
                    """,
                "answer":
                    """
                    In the current state, Link1 has an angle of -0.01 radians and is rotating counterclockwise at 0.27 radians per second, whereas Link2 has an angle of -0.01 radians relative to Link1 and is rotating clockwise at 0.61 radians per second.
                The goal is to swing the free end above the target height by applying torque on the actuator.
                Considering the current state, applying a negative torque (Action 1) will help decelerate Link1's counterclockwise rotation and Link2's clockwise rotation. 
                This will assist in swinging the free end upward, potentially bringing it closer to the target height.
                So the final answer is: apply -1 torque (Action 1).
                    """
            }
        ]


class CONSISTENCY:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: Link1: angle theta1 0.02 radians, rotating 0.01 radians per second counterclockwise. Link2: angle theta2 -0.05 radians relative to Link1, rotating 0.02 radians per second counterclockwise.
                Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0.
                Action description: Your Next Move: \n Please choose an action. Type '1' to apply -1 torque, '2' to apply 0 torque, or '3' to apply 1 torque. Ensure you provide the action number from the valid action list, i.e., [1, 2, 3].
                    """,
                "answer":
                    """
                In the current state, Link1 has an angle of 0.02 radians and is rotating counterclockwise at 0.01 radians per second. 
                Meanwhile, Link2 has an angle of -0.05 radians relative to Link1 and is also rotating counterclockwise at 0.02 radians per second. 
                The goal is to swing the free end above the target height by applying torque on the actuator.
                Given the current state, applying a positive torque (Action 3) will accelerate the counterclockwise rotation of both Link1 and Link2. 
                This will help swing the free end upward, potentially bringing it closer to the target height and improving the chances of achieving the goal.
                So the final answer is: apply 1 torque (Action 3).
                    """
            },
            {
                "question":
                    """
                State description: Current Game State: Link1: angle theta1 -0.01 radians, rotating 0.27 radians per second counterclockwise. Link2: angle theta2 -0.01 radians relative to Link1, rotating 0.61 radians per second clockwise.
                Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0
                Action description: Valid action list: [1, 2, 3]. Action 1 means to apply -1 torque, Action 2 means apply 0 torque, and Action 3 means apply 1 torque.
                    """,
                "answer":
                    """
                    In the current state, Link1 has an angle of -0.01 radians and is rotating counterclockwise at 0.27 radians per second, whereas Link2 has an angle of -0.01 radians relative to Link1 and is rotating clockwise at 0.61 radians per second.
                The goal is to swing the free end above the target height by applying torque on the actuator.
                Considering the current state, applying a negative torque (Action 1) will help decelerate Link1's counterclockwise rotation and Link2's clockwise rotation. 
                This will assist in swinging the free end upward, potentially bringing it closer to the target height.
                So the final answer is: apply -1 torque (Action 1).
                    """
            }
        ]


class SELFASK:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
            State description: Current Game State: Link1: angle theta1 0.02 radians, rotating 0.01 radians per second counterclockwise. Link2: angle theta2 -0.05 radians relative to Link1, rotating 0.02 radians per second counterclockwise.
            Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0.
            Action description: Your Next Move: \n Please choose an action. Type '1' to apply -1 torque, '2' to apply 0 torque, or '3' to apply 1 torque. Ensure you provide the action number from the valid action list, i.e., [1, 2, 3].
            """,
                "answer":
                    """
            Are follow up questions needed here: Yes.
            Follow up: What is the current angle of Link1 (theta1)?
            Intermediate answer: The current angle of Link1 is 0.02 radians.
            Follow up: What is the angular velocity of Link1?
            Intermediate answer: The angular velocity of Link1 is 0.01 radians per second counterclockwise.
            Follow up: What is the current angle of Link2 (theta2), relative to Link1?
            Intermediate answer: The current angle of Link2 relative to Link1 is -0.05 radians.
            Follow up: What is the angular velocity of Link2?
            Intermediate answer: The angular velocity of Link2 is 0.02 radians per second counterclockwise.
            Follow up: What is the current position of the free end?
            Intermediate answer: The position of the free end can be calculated using the angles and lengths of the two links. For this example, however, let us assume it has not yet reached the target height.
            Follow up: What is the task of the actuator in its current state?
            Intermediate answer: The task of the actuator is to apply torque to help swing the free end of the linear chain above the target height as soon as possible.
            Follow up: What is the optimal action for the actuator in its current state?
            Intermediate answer: Based on the current state, applying a positive torque to the actuator will help accelerate both link1 and link2 in a counterclockwise direction. This will help swing the free end upward and potentially bring it closer to the target height.
            So the final answer is: apply 1 torque (Action 3). 
            """
            },
            {
                "question":
                    """
            State description: Current Game State: Link1: angle theta1 -0.01 radians, rotating 0.27 radians per second counterclockwise. Link2: angle theta2 -0.01 radians relative to Link1, rotating 0.61 radians per second clockwise.
            Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0
            Action description: Your Next Move: \n Please choose an action. Type '1' to apply -1 torque, '2' to apply 0 torque, or '3' to apply 1 torque. Ensure you provide the action number from the valid action list, i.e., [1, 2, 3].
            """,
                "answer":
                    """
            Are follow up questions needed here: Yes.
            Follow up: What is the current angle of Link1 (theta1)?
            Intermediate answer: The current angle of Link1 is -0.01 radians.
            Follow up: What is the angular velocity of Link1?
            Intermediate answer: The angular velocity of Link1 is 0.27 radians per second counterclockwise.
            Follow up: What is the current angle of Link2 (theta2), relative to Link1?
            Intermediate answer: The current angle of Link2 relative to Link1 is -0.01 radians.
            Follow up: What is the angular velocity of Link2?
            Intermediate answer: The angular velocity of Link2 is 0.61 radians per second clockwise.
            Follow up: What is the current position of the free end?
            Intermediate answer: The position of the free end can be calculated using the angles and lengths of the two links. For this example, however, let us assume it has not yet reached the target height.
            Follow up: What is the task of the actuator in its current state?
            Intermediate answer: The task of the actuator is to apply torque to help swing the free end of the linear chain above the target height as soon as possible.
            Follow up: What is the optimal action for the actuator in its current state?
            Intermediate answer: Based on the current state, applying a negative torque to the actuator will help decelerate Link1 counterclockwise and Link2 clockwise rotation. This will help swing the free end upward and potentially bring it closer to the target height.
            So the final answer is: apply -1 torque (Action 1).
            """
            }
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
                State description: Current Game State: Link1: angle theta1 -0.04 radians, rotating 0.02 radians per second clockwise. Link2: angle theta2 0.02 radians relative to Link1, rotating 0.07 radians per second counterclockwise.
                Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0.
                Action description: Your Next Move: \n Please choose an action. Type '1' to apply -1 torque, '2' to apply 0 torque, or '3' to apply 1 torque. Ensure you provide the action number from the valid action list, i.e., [1, 2, 3].
                Your memory for the task below:
                Trial 0:
                I was trying to swing the free end of the second link above the target height by applying torques on the actuated joint. However, I did not have a clear plan of action. I should have thought about the direction of the torque and the effect of the torque on the rotation of the links. In the next trial, I will think about the direction of the torque and the effect of the torque on the rotation of the links before applying the torque.<|im_end|>
                Trial 1:
                I will apply a torque on the actuated joint in the direction that will cause the free end of the second link to swing above the target height. I will think about the effect of the torque on the rotation of the links before applying the torque.<|im_end|>
                Trial 2:
                I will continue to apply a torque on the actuated joint in the direction that will cause the free end of the second link to swing above the target height. I will think about the effect of the torque on the rotation of the links before applying the torque.<|im_end|>
                    """,
                "answer":
                    """
                Based on the current game state and memories, the optimal action for the player to take would be to apply -1 torque (Action 1). Therefore, the optimal action to take now is to apply -1 torque (Action 1).
                    """
            },
            {
                "question":
                    """
                State description: Current Game State: Link1: angle theta1 0.31 radians, rotating 0.76 radians per second clockwise. Link2: angle theta2 -0.73 radians relative to Link1, rotating 0.98 radians per second counterclockwise.
                Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0.
                Action description: Your Next Move: \n Please choose an action. Type '1' to apply -1 torque, '2' to apply 0 torque, or '3' to apply 1 torque. Ensure you provide the action number from the valid action list, i.e., [1, 2, 3].
                Your memory for the task below:
                Trial 0:
                I will apply a torque on the actuated joint in the direction that will cause the free end of the second link to swing above the target height. I will think about the effect of the torque on the rotation of the links before applying the torque.<|im_end|>
                Trial 1:
                I will continue to apply a torque on the actuated joint in the direction that will cause the free end of the second link to swing above the target height. I will think about the effect of the torque on the rotation of the links before applying the torque.<|im_end|>
                Trial 2:
                In this environment, my plan was to apply a torque on the actuated joint in the direction that will cause the free end of the second link to swing above the target height. However, I did not think about the effect of the torque on the rotation of the links before applying the torque. In the next trial, I will think about the effect of the torque on the rotation of the links before applying the torque.<|im_end|>
                    """,
                "answer":
                    """
                Based on the current game state and memories, the optimal action for the player to take would be to apply 1 torque (Action 3). Therefore, the optimal action to take now is to apply 1 torque (Action 3).
                    """
            },
        ]

class EGG:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: Link1: angle theta1 -0.04 radians, rotating 0.02 radians per second clockwise. Link2: angle theta2 0.02 radians relative to Link1, rotating 0.07 radians per second counterclockwise.
                Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0.
                Action description: Your Next Move: \n Please choose an action. Type '1' to apply -1 torque, '2' to apply 0 torque, or '3' to apply 1 torque. Ensure you provide the action number from the valid action list, i.e., [1, 2, 3].
                The insights of the game are listed below: The key information that can be exploited to improve the player's performance is that the current policy of consistently applying torque in one direction is not effective in achieving the goal of swinging the free end of the linear chain above the target height. The player may benefit from exploring different torque values and directions and adjusting its torque based on the current state of the system, such as the angles and angular velocities of the links. This information can be used to inform a more adaptive and effective policy, potentially using techniques such as reinforcement learning or model-based control.
                The suggestions are listed below:
                1. Exploration:
                - The player should explore different torque values and directions to find the optimal policy.
                - To make the exploration, the player can randomly choose torque values and directions for a certain number of steps, then evaluate the performance and adjust the policy accordingly.

                2. Exploitation:
                - The player should adjust the torque based on the current state of the system, such as the angles and angular velocities of the links.
                - The player should also try to apply torque in a way that helps swing the free end of the linear chain above the target height.
                - To improve the policy, the player can use techniques such as reinforcement learning or model-based control.

                3. Weighting:
                - The player should focus more on exploration in the beginning of the episode to find the optimal policy.
                - As the episode progresses, the player should shift the focus towards exploitation to gain a higher performance.
                - The player should also adjust the weighting based on the performance and adjust the policy accordingly.
                    """,
                "answer":
                    """
                Based on the current game state, the insights and the suggestions, the optimal action for the player to take would be to apply -1 torque (Action 1). Therefore, the optimal action to take now is to apply -1 torque (Action 1).
                    """
            },{
                "question":
                    """
                State description: Current Game State: Link1: angle theta1 0.31 radians, rotating 0.76 radians per second clockwise. Link2: angle theta2 -0.73 radians relative to Link1, rotating 0.98 radians per second counterclockwise.
                Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0.
                Action description: Your Next Move: \n Please choose an action. Type '1' to apply -1 torque, '2' to apply 0 torque, or '3' to apply 1 torque. Ensure you provide the action number from the valid action list, i.e., [1, 2, 3].
                The insights of the game are listed below: The key information that can be exploited to improve the performance of the player is that the current policy of consistently applying torque in one direction is not effective in achieving the goal of swinging the free end of the linear chain above the target height. The player may benefit from exploring different torque values and directions and adjusting its torque based on the current state of the system, such as the angles and angular velocities of the links. This information can be used to inform a more adaptive and effective policy, potentially using techniques such as reinforcement learning or model-based control.
                The suggestions are listed below:
                1. Exploration: 
                - The player should explore different torque values and directions, rather than sticking to a consistent pattern. 
                - The player should also adjust the torque based on the current state of the system, such as the angles and angular velocities of the links. 
                - To make the exploration, the player can randomly choose torque values and directions, or try to systematically vary the torque values and directions to cover a wider range of possibilities.

                2. Exploitation: 
                - The player should use the information obtained from exploration to inform a more adaptive and effective policy. 
                - The player can use techniques such as reinforcement learning or model-based control to improve the policy. 
                - The policy should take into account the current state of the system, such as the angles and angular velocities of the links, to adjust the torque values and directions accordingly.

                3. Weighting for exploration and exploitation: 
                - The player should balance exploration and exploitation to find the optimal policy. 
                - In the beginning of the episode, the player should focus more on exploration to gather information about the system and find a wider range of possible solutions. 
                - As the episode progresses, the player should shift the focus towards exploitation to improve the policy and achieve a higher performance. 
                - The weighting can be adjusted
                    """,
                "answer":
                    """
                Based on the current game state, the insights and the suggestions, the optimal action for the player to take would be to apply 1 torque (Action 3). Therefore, the optimal action to take now is to apply 1 torque (Action 3).
                    """
            },
        ]

class EGGWithoutInsights:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: Link1: angle theta1 -0.04 radians, rotating 0.02 radians per second clockwise. Link2: angle theta2 0.02 radians relative to Link1, rotating 0.07 radians per second counterclockwise.
                Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0.
                Action description: Your Next Move: \n Please choose an action. Type '1' to apply -1 torque, '2' to apply 0 torque, or '3' to apply 1 torque. Ensure you provide the action number from the valid action list, i.e., [1, 2, 3].
                The suggestions are listed below:
                1. Exploration:
                - The player should explore different torque values and directions to find the optimal policy.
                - To make the exploration, the player can randomly choose torque values and directions for a certain number of steps, then evaluate the performance and adjust the policy accordingly.

                2. Exploitation:
                - The player should adjust the torque based on the current state of the system, such as the angles and angular velocities of the links.
                - The player should also try to apply torque in a way that helps swing the free end of the linear chain above the target height.
                - To improve the policy, the player can use techniques such as reinforcement learning or model-based control.

                3. Weighting:
                - The player should focus more on exploration in the beginning of the episode to find the optimal policy.
                - As the episode progresses, the player should shift the focus towards exploitation to gain a higher performance.
                - The player should also adjust the weighting based on the performance and adjust the policy accordingly.
                    """,
                "answer":
                    """
                Based on the current game state and the suggestions, the optimal action for the player to take would be to apply -1 torque (Action 1). Therefore, the optimal action to take now is to apply -1 torque (Action 1).
                    """
            },{
                "question":
                    """
                State description: Current Game State: Link1: angle theta1 0.31 radians, rotating 0.76 radians per second clockwise. Link2: angle theta2 -0.73 radians relative to Link1, rotating 0.98 radians per second counterclockwise.
                Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0.
                Action description: Your Next Move: \n Please choose an action. Type '1' to apply -1 torque, '2' to apply 0 torque, or '3' to apply 1 torque. Ensure you provide the action number from the valid action list, i.e., [1, 2, 3].
                The suggestions are listed below:
                1. Exploration: 
                - The player should explore different torque values and directions, rather than sticking to a consistent pattern. 
                - The player should also adjust the torque based on the current state of the system, such as the angles and angular velocities of the links. 
                - To make the exploration, the player can randomly choose torque values and directions, or try to systematically vary the torque values and directions to cover a wider range of possibilities.

                2. Exploitation: 
                - The player should use the information obtained from exploration to inform a more adaptive and effective policy. 
                - The player can use techniques such as reinforcement learning or model-based control to improve the policy. 
                - The policy should take into account the current state of the system, such as the angles and angular velocities of the links, to adjust the torque values and directions accordingly.

                3. Weighting for exploration and exploitation: 
                - The player should balance exploration and exploitation to find the optimal policy. 
                - In the beginning of the episode, the player should focus more on exploration to gather information about the system and find a wider range of possible solutions. 
                - As the episode progresses, the player should shift the focus towards exploitation to improve the policy and achieve a higher performance. 
                - The weighting can be adjusted
                    """,
                "answer":
                    """
                Based on the current game state and the suggestions, the optimal action for the player to take would be to apply 1 torque (Action 3). Therefore, the optimal action to take now is to apply 1 torque (Action 3).
                    """
            },
        ]

class EGGWithoutSuggestions:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: Link1: angle theta1 -0.04 radians, rotating 0.02 radians per second clockwise. Link2: angle theta2 0.02 radians relative to Link1, rotating 0.07 radians per second counterclockwise.
                Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0.
                Action description: Your Next Move: \n Please choose an action. Type '1' to apply -1 torque, '2' to apply 0 torque, or '3' to apply 1 torque. Ensure you provide the action number from the valid action list, i.e., [1, 2, 3].
                The insights of the game are listed below: The key information that can be exploited to improve the player's performance is that the current policy of consistently applying torque in one direction is not effective in achieving the goal of swinging the free end of the linear chain above the target height. The player may benefit from exploring different torque values and directions and adjusting its torque based on the current state of the system, such as the angles and angular velocities of the links. This information can be used to inform a more adaptive and effective policy, potentially using techniques such as reinforcement learning or model-based control.
                    """,
                "answer":
                    """
                Based on the current game state and the insights, the optimal action for the player to take would be to apply -1 torque (Action 1). Therefore, the optimal action to take now is to apply -1 torque (Action 1).
                    """
            },{
                "question":
                    """
                State description: Current Game State: Link1: angle theta1 0.31 radians, rotating 0.76 radians per second clockwise. Link2: angle theta2 -0.73 radians relative to Link1, rotating 0.98 radians per second counterclockwise.
                Goal description: The goal is to apply torque on the actuator to swing the free end of the linear chain above the target height, which is constructed as: -cos(theta1) - cos(theta2 + theta1) > 1.0.
                Action description: Your Next Move: \n Please choose an action. Type '1' to apply -1 torque, '2' to apply 0 torque, or '3' to apply 1 torque. Ensure you provide the action number from the valid action list, i.e., [1, 2, 3].
                The insights of the game are listed below: The key information that can be exploited to improve the performance of the player is that the current policy of consistently applying torque in one direction is not effective in achieving the goal of swinging the free end of the linear chain above the target height. The player may benefit from exploring different torque values and directions and adjusting its torque based on the current state of the system, such as the angles and angular velocities of the links. This information can be used to inform a more adaptive and effective policy, potentially using techniques such as reinforcement learning or model-based control.
                    """,
                "answer":
                    """
                Based on the current game state and the insights, the optimal action for the player to take would be to apply 1 torque (Action 3). Therefore, the optimal action to take now is to apply 1 torque (Action 3).
                    """
            },
        ]