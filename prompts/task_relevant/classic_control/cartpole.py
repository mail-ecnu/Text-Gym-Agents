class ACT:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
            State description: The current state is: The cart is at position 0.01, moving at velocity 0.01. The pole is tilted at an angle of -0.05 radians, and rotating at -0.00 radians per second.
            Goal description: The goal is to keep the pole balanced upright for as long as possible.
            Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right.
                    """,
                "answer":
                    """The final answer is: Push the cart to the left (Action 1). """
            },
            {
                "question":
                    """
            State description: The current state is: The cart is at position -0.04, moving at velocity 0.01. The pole is tilted at an angle of 0.12 radians, and rotating at 0.13 radians per second.
            Goal description: The goal is to keep the pole balanced upright for as long as possible.
            Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right.
                    """,
                "answer":
                    """The final answer is: Push the cart to the right (Action 2). """
            },
        ]

class COT:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
    State description: The current state is: The cart is at position 0.01, moving at velocity 0.01. The pole is tilted at an angle of -0.05 radians, and rotating at -0.00 radians per second.
    Goal description: The goal is to keep the pole balanced upright for as long as possible.
    Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right.
    """,
                "answer":
                    """The cart is in position 0.01, right of the center of the interval (-2.4, 2.4), and also has a velocity
                of 0.01 to the right, so it is more reasonable to push the cart to the left. The pole on the cart is
                tilted 0.05 radians to the left, and there is no angular velocity tilted to the left, so it is more
                reasonable to push the cart to the left.Combining the above two conditions, the action of pushing the
                cart to the right is more reasonable. So the final answer is: Push the cart to the left (Action 1). """
            },
            {
                "question":
                    """
    State description: The current state is: The cart is at position -0.04, moving at velocity 0.01. The pole is tilted at an angle of 0.12 radians, and rotating at 0.13 radians per second.
    Goal description: The goal is to keep the pole balanced upright for as long as possible.
    Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right.
    """,
                "answer":
                    """The cart is in position -0.04, left of the center of the interval (-2.4, 2.4), and also has a velocity
                of 0.01 to the right, so it is more reasonable to push the cart to the right. The pole on the cart is
                tilted 0.12 radians to the right, and has an angular velocity of 0.13 radians/s to the right,
                so it is more reasonable to push the cart to the right. Combining the above two conditions,
                since the balance of the pole on the cart is more important than the position of the cart, the action of
                pushing the cart to the right is more reasonable. So the final answer is: Push the cart to the right (
                Action 2). """
            },
        ]


class PAL:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: The current state is: The cart is at position -0.04, moving at velocity 0.01. The pole is tilted at 0.12 radians, rotating at 0.13 radians per second towards the right.
                Goal description: The goal is to keep the pole balanced upright for as long as possible.
                Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right.
                    """,
                "answer":
                    """
                upper_position_range = 2.4
                upper_angle_range = 0.2095
                position_importance_ratio = 0.5
                # The cart is in position -0.04, and has a velocity of 0.01 to the right.
                next_step_position = current_cart_position + current_cart_velocity
                # Based on the position of the cart, the direction of pushing the cart is
                if(next_step_position < 0):
                    push_direction_position = 2
                else:
                    push_direction_position = 1
                # The importance of the location of the cart is
                position_importance = math.abs(next_step_position) / upper_position_range * position_importance_ratio
                # The pole is tilted at 0.12 radians, rotating at 0.13 radians per second towards the right.
                next_pole_angle = current_pole_angle + angular_velocity                                                          
                # Based on the angle of the pole, the direction of pushing the cart is
                if(next_pole_angle < 0):
                    push_direction_angle = 1
                else:
                    push_direction_angle = 2
                # The importance of the angle of the pole is
                # pole_angle_importance = math.abs(next_pole_angle) / upper_angle_range
                # Comparing positional and angular importance
                # position_importance = 0.0625
                # pole_angle_importance = 1.1933
                if(position_importance > pole_angle_importance):
                    push_direction = push_direction_position
                else:
                    push_direction = push_direction_angle
                # Because (position_importance < pole_angle_importance) and (next_pole_angle > 0)
                print("Action :", push_direction)
                # So the final answer is: Push the cart to the right (Action 2).
                    """
            },{"question":
                    """
                State description: The current state is: The cart is at position 0.01, moving at velocity 0.01. The pole is tilted at an angle of -0.05 radians, and rotating at -0.00 radians per second.
                Goal description: The goal is to keep the pole balanced upright for as long as possible.
                Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right.
                    """,
                "answer":
                    """
                upper_position_range = 2.4
                upper_angle_range = 0.2095
                position_importance_ratio = 0.5
                # The cart is in position 0.01, and has a velocity of 0.01 to the right.
                next_step_position = current_cart_position + current_cart_velocity
                # Based on the position of the cart, the direction of pushing the cart is
                if(next_step_position < 0):
                    push_direction_position = 2
                else:
                    push_direction_position = 1
                # The importance of the location of the cart is
                position_importance = math.abs(next_step_position) / upper_position_range * position_importance_ratio
                # The pole is tilted at -0.05 radians, rotating at 0.00 radians per second towards the right.
                next_pole_angle = current_pole_angle + angular_velocity                                                           
                # Based on the angle of the pole, the direction of pushing the cart is
                if(next_pole_angle < 0):
                    push_direction_angle = 1
                else:
                    push_direction_angle = 2
                # The importance of the angle of the pole is
                pole_angle_importance = math.abs(next_pole_angle) / upper_angle_range
                # Comparing positional and angular importance
                # position_importance = 0.0041
                # pole_angle_importance = 0.2386
                if(position_importance > pole_angle_importance):
                    push_direction = push_direction_position
                else:
                    push_direction = push_direction_angle
                # Because (position_importance < pole_angle_importance) and (next_pole_angle > 0)
                print("Action :", push_direction)
                # So the final answer is: Push the cart to the left (Action 1).
                    """
            }
        ]


class CONSISTENCY:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
        State description: The current state is: The cart is at position 0.01, moving at velocity 0.01. The pole is tilted at an angle of -0.05 radians, and rotating at -0.00 radians per second.
        Goal description: The goal is to keep the pole balanced upright for as long as possible.
        Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right.
        """,
                "answer":
                    """
        The cart is in position 0.01, right of the center of the interval (-2.4, 2.4), and also has a velocity of 0.01 to the right, so it is more reasonable to push the cart to the left. The pole on the cart is tilted 0.05 radians to the left, and there is no angular velocity tilted to the left, so it is more reasonable to push the cart to the left. Combining the above two conditions, the action of pushing the cart to the right is more reasonable. So the final answer is: Push the cart to the left (Action 1). 
        """
            },
            {
                "question":
                    """
        State description: The current state is: The cart is at position -0.04, moving at velocity 0.01. The pole is tilted at an angle of 0.12 radians, and rotating at 0.13 radians per second.
        Goal description: The goal is to keep the pole balanced upright for as long as possible.
        Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right.
        """,
                "answer":
                    """
        The cart is in position -0.04, left of the center of the interval (-2.4, 2.4), and also has a velocity of 0.01 to the right, so it is more reasonable to push the cart to the right. The pole on the cart is tilted 0.12 radians to the right, and has an angular velocity of 0.13 radians/s to the right, so it is more reasonable to push the cart to the right. Combining the above two conditions, since the balance of the pole on the cart is more important than the position of the cart, the action of pushing the cart to the right is more reasonable. So the final answer is: Push the cart to the right (Action 2). 
        """
            },
        ]


class SELFASK:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
            State description: The current state is: The cart is at position 0.01, moving at velocity 0.01. The pole is tilted at an angle of -0.05 radians, and rotating at -0.00 radians per second.
            Goal description: The goal is to keep the pole balanced upright for as long as possible.
            Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right. 
            """,
                "answer":
                    """
            Are follow up questions needed here: Yes.
            Follow up: In which direction is the pole tilted?
            Intermediate answer: The pole is rotating at -0.00 radians per second, so the pole stays balanced.
            Follow up: How can the tendency of the pole to move be counteracted?
            Intermediate answer: Pushing the cart in the opposite direction will exacerbate pole tilts, so we need to push the cart in the same direction as the pole is tilted.
            Follow up: So which direction to push the cart?
            Intermediate answer: Left or right, since the pole is balanced.
            Follow up: In which direction is the cart moving?
            Intermediate answer: Velocity is 0.01, positive, so moving right.
            Follow up: How can the tendency of the cart to move be counteracted?
            Intermediate answer: Pushing the cart in the same direction will exacerbate cart moving, so we need to push the cart in the opposite direction.
            Follow up: So which direction to push the cart?
            Intermediate answer: Left.
            Follow up: Which is more important, the balance of the pole or the position of the car?
            Intermediate answer: Position of the car, since the pole is already in balance, and the car is at 0.01 with velocity 0.01 so far, it will be out of valid range [-2.4, 2.4] faster than the pole.
            So the final answer is: Push the cart to the left (Action 1).
            """
            },
            {
                "question":
                    """
            State description: The current state is: The cart is at position -0.04, moving at velocity 0.01. The pole is tilted at an angle of 0.12 radians, and rotating at 0.13 radians per second.
            Goal description: The goal is to keep the pole balanced upright for as long as possible.
            Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right. 
            """,
                "answer":
                    """
            Are follow up questions needed here: Yes.
            Follow up: In which direction is the pole tilted?
            Intermediate answer: Rotating velocity is 0.13 radians per second, positive, so tilting right.
            Follow up: How can the tendency of the pole to move be counteracted?
            Intermediate answer: Pushing the cart in the opposite direction will exacerbate pole tilts, so we need to push the cart in the same direction as the pole is tilted.
            Follow up: So which direction to push the cart?
            Intermediate answer: Right.
            Follow up: In which direction is the cart moving?
            Intermediate answer: Velocity is 0.01, positive, so moving right.
            Follow up: How can the tendency of the cart to move be counteracted?
            Intermediate answer: Pushing the cart in the same direction will exacerbate cart moving, so we need to push the cart in the opposite direction.
            Follow up: So which direction to push the cart?
            Intermediate answer: Left.
            Follow up: Which is more important, the balance of the pole or the position of the car?
            Intermediate answer: Balance of the pole, since the pole is tilted at an angle of 0.12 radians, and rotating at 0.13 radians per second so far, it will be out of vaild range [-0.2095, 0.2095] faster than the cart.
            So the final answer is: Push the cart to the right (Action 2).
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
                State description: The current state is: The cart is positioned at -0.053, with a velocity of 0.01 towards the right. The pole is tilted at 0.05 radians, rotating at 0.11 radians per second towards the right.
                Goal description: The goal is to keep the pole balanced upright for as long as possible.
                Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right. 
                Your memory for the task below:
                Trial 0:
                I was not able to keep the pole balanced upright for as long as possible. I should have tried to move the cart left or right to keep the pole balanced. In the next trial, I will try to move the cart left or right to keep the pole balanced.<|im_end|>
                Trial 1:
                In this environment, my plan was to move the cart left or right to keep the pole balanced. However, I did not have a specific strategy for moving the cart. In the next trial, I will try to move the cart left or right based on the pole angle. If the pole is tilted to the left, I will move the cart to the left. If the pole is tilted to the right, I will move the cart to the right.<|im_end|>
                Trial 2:
                In this environment, my plan was to move the cart left or right based on the pole angle. However, I did not have a specific strategy for moving the cart. In the next trial, I will try to move the cart left or right based on the pole angle and the cart position. If the pole is tilted to the left and the cart is to the left of center, I will move the cart to the right. If the pole is tilted to the left and the cart is to the right of center, I will move the cart to the left. If the pole is tilted to the right and the cart is to the left of center, I will move the cart to the left. If the pole is tilted to the right and the cart is to the right of center, I will move the cart to the right.<|im_end|>
                    """,
                "answer":
                    """
                Based on the current game state and memories of the task, the optimal action for the player to take would be to push the cart to the right (action 2) to maintain balance of the pole. Therefore, the optimal action to take now is to push the cart to the right (action 2).
                    """
            },
            {
                "question":
                    """
                State description: The current state is: The cart is positioned at 0.033, with a velocity of 0.05 towards the left. The pole is tilted at 0.02 radians, rotating at 0.03 radians per second towards the right.
                Goal description: The goal is to keep the pole balanced upright for as long as possible.
                Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right. 
                Your memory for the task below:
                Trial 0:
                In this environment, my plan was to move the cart left or right to keep the pole balanced. However, I did not have a specific strategy for moving the cart. In the next trial, I will try to move the cart left or right based on the pole angle. If the pole is tilted to the left, I will move the cart to the left. If the pole is tilted to the right, I will move the cart to the right.<|im_end|>
                Trial 1:
                In this environment, my plan was to move the cart left or right based on the pole angle. However, I did not have a specific strategy for moving the cart. In the next trial, I will try to move the cart left or right based on the pole angle and the cart position. If the pole is tilted to the left and the cart is to the left of center, I will move the cart to the right. If the pole is tilted to the left and the cart is to the right of center, I will move the cart to the left. If the pole is tilted to the right and the cart is to the left of center, I will move the cart to the left. If the pole is tilted to the right and the cart is to the right of center, I will move the cart to the right.<|im_end|>
                Trial 2:
                In the next trial, I will move the cart left or right based on the pole angle and the cart position. If the pole is tilted to the left and the cart is to the left of center, I will move the cart to the right. If the pole is tilted to the left and the cart is to the right of center, I will move the cart to the left. If the pole is tilted to the right and the cart is to the left of center, I will move the cart to the left. If the pole is tilted to the right and the cart is to the right of center, I will move the cart to the right.<|im_end|>
                    """,
                "answer":
                    """
                Based on the current game state and memories of the task, the optimal action for the player to take would be to push the cart to the right (action 2) to maintain balance of the pole. Therefore, the optimal action to take now is to push the cart to the right (action 2).
                    """
            },
        ]

class EGG:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: The current state is: The cart is positioned at -0.053, with a velocity of 0.01 towards the right. The pole is tilted at 0.05 radians, rotating at 0.11 radians per second towards the right.
                Goal description: The goal is to keep the pole balanced upright for as long as possible.
                Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right. 
                The insights of the game are listed below: The key information that can be exploited to improve performance of the player includes the fact that the policy alternates between moving the cart left and right based on the pole's tilt, but struggles to recover from large tilts of the pole. Additionally, the velocity of the cart increases rapidly towards the end of the game, indicating that the policy may not be able to keep up with the increasing difficulty of the game. To improve performance, the policy can be adjusted to take into account the increasing velocity of the cart or a different algorithm can be used. Incorporating a mechanism for learning from past mistakes, such as experience replay, may also be beneficial.
                The suggestions are listed below:Suggestion for the next episode:
                1. Exploration: The player should explore different strategies for recovering from large tilts of the pole. This can be done by trying out different actions when the pole is tilted beyond a certain angle, such as moving the cart in the opposite direction or applying a stronger force. The player can also try to observe the behavior of the pole and cart in different situations to gain a better understanding of the dynamics of the game.
                2. Exploitation: To improve performance, the player can adjust the policy to take into account the increasing velocity of the cart towards the end of the game. This can be done by increasing the sensitivity of the policy to changes in the velocity of the cart, or by using a different algorithm that is better suited to handling non-stationary environments. Additionally, the player can incorporate a mechanism for learning from past mistakes, such as experience replay, to help the policy recover from large tilts of the pole.
                3. Weighting: The player should focus more on exploitation than exploration in the next episode, as they have already explored different strategies in the previous episodes. However, they should still allocate some time for exploration to gain a better understanding of the dynamics of the game and to try out new strategies for recovering from large til
                    """,
                "answer":
                    """
                Based on the current game state, the insights and the suggestions, the optimal action for the player to take would be to push the cart to the right (action 2) to maintain balance of the pole. Therefore, the optimal action to take now is to push the cart to the right (action 2).
                    """
            },{
                "question":
                    """
                State description: The current state is: The cart is positioned at 0.033, with a velocity of 0.05 towards the left. The pole is tilted at 0.02 radians, rotating at 0.03 radians per second towards the right.
                Goal description: The goal is to keep the pole balanced upright for as long as possible.
                Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right. 
                The insights of the game are listed below: The key information that can be exploited to improve performance of the player includes the fact that the policy alternates between moving the cart left and right based on the pole's tilt, but struggles to recover from large tilts of the pole. Additionally, the velocity of the cart increases rapidly towards the end of the game, which may indicate that the policy is not able to keep up with the increasing difficulty of the game. To improve performance, the policy can be adjusted to take into account the increasing velocity of the cart or a different algorithm can be used. Incorporating a mechanism for learning from past mistakes, such as experience replay, may also be beneficial.
                The suggestions are listed below:
                1. For exploration, the player should try to experiment with different action sequences to see if there are any patterns that lead to longer pole balancing times. One way to do this is to randomly select actions for a certain number of steps before returning to the current policy. 
                2. To improve policy performance, the player can try incorporating a mechanism for learning from past mistakes, such as experience replay. Additionally, the policy can be adjusted to take into account the increasing velocity of the cart by adding a penalty for large changes in cart velocity. 
                3. The player should focus more on exploitation than exploration in the next episode, as they have already tried multiple exploration strategies in previous episodes. However, they should still allocate a small portion of their actions to exploration to avoid getting stuck in a suboptimal policy. A good ratio to start with could be 80% exploitation and 20% exploration.
                    """,
                "answer":
                    """
                Based on the current game state, the insights and the suggestions, the optimal action for the player to take would be to push the cart to the right (action 2) to maintain balance of the pole. Therefore, the optimal action to take now is to push the cart to the right (action 2).
                    """
            },
        ]

class EGGWithoutInsights:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: The current state is: The cart is positioned at -0.053, with a velocity of 0.01 towards the right. The pole is tilted at 0.05 radians, rotating at 0.11 radians per second towards the right.
                Goal description: The goal is to keep the pole balanced upright for as long as possible.
                Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right. 
                The suggestions are listed below:Suggestion for the next episode:
                1. Exploration: The player should explore different strategies for recovering from large tilts of the pole. This can be done by trying out different actions when the pole is tilted beyond a certain angle, such as moving the cart in the opposite direction or applying a stronger force. The player can also try to observe the behavior of the pole and cart in different situations to gain a better understanding of the dynamics of the game.
                2. Exploitation: To improve performance, the player can adjust the policy to take into account the increasing velocity of the cart towards the end of the game. This can be done by increasing the sensitivity of the policy to changes in the velocity of the cart, or by using a different algorithm that is better suited to handling non-stationary environments. Additionally, the player can incorporate a mechanism for learning from past mistakes, such as experience replay, to help the policy recover from large tilts of the pole.
                3. Weighting: The player should focus more on exploitation than exploration in the next episode, as they have already explored different strategies in the previous episodes. However, they should still allocate some time for exploration to gain a better understanding of the dynamics of the game and to try out new strategies for recovering from large til
                    """,
                "answer":
                    """
                Based on the current game state and the suggestions, the optimal action for the player to take would be to push the cart to the right (action 2) to maintain balance of the pole. Therefore, the optimal action to take now is to push the cart to the right (action 2).
                    """
            },{
                "question":
                    """
                State description: The current state is: The cart is positioned at 0.033, with a velocity of 0.05 towards the left. The pole is tilted at 0.02 radians, rotating at 0.03 radians per second towards the right.
                Goal description: The goal is to keep the pole balanced upright for as long as possible.
                Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right. 
                The suggestions are listed below:
                1. For exploration, the player should try to experiment with different action sequences to see if there are any patterns that lead to longer pole balancing times. One way to do this is to randomly select actions for a certain number of steps before returning to the current policy. 
                2. To improve policy performance, the player can try incorporating a mechanism for learning from past mistakes, such as experience replay. Additionally, the policy can be adjusted to take into account the increasing velocity of the cart by adding a penalty for large changes in cart velocity. 
                3. The player should focus more on exploitation than exploration in the next episode, as they have already tried multiple exploration strategies in previous episodes. However, they should still allocate a small portion of their actions to exploration to avoid getting stuck in a suboptimal policy. A good ratio to start with could be 80% exploitation and 20% exploration.
                    """,
                "answer":
                    """
                Based on the current game state and the suggestions, the optimal action for the player to take would be to push the cart to the right (action 2) to maintain balance of the pole. Therefore, the optimal action to take now is to push the cart to the right (action 2).
                    """
            },
        ]

class EGGWithoutSuggestions:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: The current state is: The cart is positioned at -0.053, with a velocity of 0.01 towards the right. The pole is tilted at 0.05 radians, rotating at 0.11 radians per second towards the right.
                Goal description: The goal is to keep the pole balanced upright for as long as possible.
                Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right. 
                The insights of the game are listed below: The key information that can be exploited to improve performance of the player includes the fact that the policy alternates between moving the cart left and right based on the pole's tilt, but struggles to recover from large tilts of the pole. Additionally, the velocity of the cart increases rapidly towards the end of the game, indicating that the policy may not be able to keep up with the increasing difficulty of the game. To improve performance, the policy can be adjusted to take into account the increasing velocity of the cart or a different algorithm can be used. Incorporating a mechanism for learning from past mistakes, such as experience replay, may also be beneficial.
                    """,
                "answer":
                    """
                Based on the current game state and the insights, the optimal action for the player to take would be to push the cart to the right (action 2) to maintain balance of the pole. Therefore, the optimal action to take now is to push the cart to the right (action 2).
                    """
            },{
                "question":
                    """
                State description: The current state is: The cart is positioned at 0.033, with a velocity of 0.05 towards the left. The pole is tilted at 0.02 radians, rotating at 0.03 radians per second towards the right.
                Goal description: The goal is to keep the pole balanced upright for as long as possible.
                Action description: Valid action list: [1, 2]. Action 1 means to push the cart to the left, and Action 2 means push the cart to the right. 
                The insights of the game are listed below: The key information that can be exploited to improve performance of the player includes the fact that the policy alternates between moving the cart left and right based on the pole's tilt, but struggles to recover from large tilts of the pole. Additionally, the velocity of the cart increases rapidly towards the end of the game, which may indicate that the policy is not able to keep up with the increasing difficulty of the game. To improve performance, the policy can be adjusted to take into account the increasing velocity of the cart or a different algorithm can be used. Incorporating a mechanism for learning from past mistakes, such as experience replay, may also be beneficial.
                    """,
                "answer":
                    """
                Based on the current game state and the insights, the optimal action for the player to take would be to push the cart to the right (action 2) to maintain balance of the pole. Therefore, the optimal action to take now is to push the cart to the right (action 2).
                    """
            },
        ]