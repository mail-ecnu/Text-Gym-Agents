class ACT:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
            State description: The lander is at position (-0.01, 1.39), the horizontal speed of movement is -0.65, the vertical velocity speed of movement is -0.41. The angle is 0.01 radians, and it's rotating at 0.13 radians per second. The left leg is not in contact with ground. The right leg is not in contact with ground.
            Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
            Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            The final answer is fire the main engine (operation 3).
            """
            },
            {
                "question":
                    """
            State description: The lander is at position (-0.99, 0.43), the horizontal speed of movement is -2.02, the vertical velocity speed of movement is -0.81. The angle is 0.71 radians, and it's rotating at -0.21 radians per second. The left leg is not in contact with ground. The right leg is not in contact with ground.
            Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
            Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            The final answer is fire the main engine (operation 3).
            """
            }
        ]


class COT:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
            State description: The lander is at position (-0.01, 1.39), the horizontal speed of movement is -0.65, the vertical velocity speed of movement is -0.41. The angle is 0.01 radians, and it's rotating at 0.13 radians per second. The left leg is not in contact with ground. The right leg is not in contact with ground.
            Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
            Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            According to the current state description, the lander is moving to the left at a high horizontal velocity and needs to reduce its horizontal velocity to land safely. However, at the same time, the lander is landing at a higher velocity of 0.41. Therefore, we can choose operation 3 (fire the main engine) to reduce the descent velocity. Therefore, the final answer is fire the main engine (operation 3).
            """
            },
            {
                "question":
                    """
            State description: The lander is at position (-0.99, 0.43), the horizontal speed of movement is -2.02, the vertical velocity speed of movement is -0.81. The angle is 0.71 radians, and it's rotating at -0.21 radians per second. The left leg is not in contact with ground. The right leg is not in contact with ground.
            Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
            Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            According to the current state description, the lander is moving to the left at a high horizontal velocity and needs to reduce its horizontal velocity to land safely. However, at the same time, the lander is landing at a higher velocity of 0.81. Therefore, we can choose operation 3 (fire the main engine) to reduce the descent velocity. Therefore, the final answer is fire the main engine (operation 3).
            """
            }
        ]


class PAL:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
            State description: The lander is at position (-0.01, 1.39), the horizontal speed of movement is -0.65, the vertical velocity speed of movement is -0.41. The angle is 0.01 radians, and it's rotating at 0.13 radians per second. The left leg is not in contact with ground. The right leg is not in contact with ground.
            Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
            Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
                import random
                import math
                
                def decide_action(state):
                    # 获取当前状态下的关键信息
                    pos_x, pos_y = state[0]
                    speed_x, speed_y = state[1]
                    angle = state[2][0]
                    angular_vel = state[3][0]
                    left_leg_contact, right_leg_contact = state[4]
                    
                    # 设定目标区域的位置
                    target_pos = (0, 0)
                
                    # 根据目标位置与当前位置之间的关系，选择下一步的动作
                    if pos_y > target_pos[1] + 0.5 or abs(pos_x - target_pos[0]) > 0.4:
                        # 如果距离目标位置太远，就向上方和两侧移动
                        if abs(angle) > 0.4:
                            # 如果当前角度不够稳定，就继续调整角度
                            if angle > 0:
                                return 1  # 向右侧移动，使用左引擎
                            else:
                                return 3  # 向左侧移动，使用右引擎
                        else:
                            # 如果角度在可接受区间内，就开启主引擎向上移动
                            return 2
                    elif abs(speed_y) > 5 or abs(speed_x) > 1:
                        # 如果距离目标位置比较近，但速度仍然比较快，就继续调整速度和角度
                        if abs(angle) > 0.1:
                            # 如果角度不够稳定，则继续调整角度
                            if angle > 0:
                                return 1  # 向右侧移动，使用左引擎
                            else:
                                return 3  # 向左侧移动，使用右引擎
                        else:
                            # 如果速度方向偏离目标方向，则使用侧引擎调整速度
                            if speed_x < 0:
                                return 1  # 向右侧调整速度，使用左引擎
                            else:
                                return 3  # 向左侧调整速度，使用右引擎
                    else:
                        # 如果距离合适，速度较慢，就需要调整姿态使得两条腿关闭
                        if not (left_leg_contact and right_leg_contact):
                            # 如果有一个腿没有关闭，就用偏转引擎调整姿态
                            if angle > 0.1:
                                # 左倾斜，就向右侧旋转，使用左引擎
                                return 1
                            elif angle < -0.1:
                                # 右倾斜，就向左侧旋转，使用右引擎
                                return 3
                            else:
                                # 可以调整姿态
                                if left_leg_contact:
                                    # 右腿没有关闭，就向左侧旋转，使用右引擎
                                    return 3
                                else:
                                    # 左腿没有关闭，就向右侧旋转，使用左引擎
                                    return 1
                        else:
                            # 如果两条腿都关闭，则需要让LunarLander平稳着陆。首先根据竖直方向上的速度来判断
                            if abs(speed_y) > 1:
                                if speed_y < 0:
                                    # 向上移动，使用主引擎
                                    return 2
                                else:
                                    # 向下移动，则关闭引擎
                                    return 0
                            else:
                                # 竖直方向上的速度已经足够小，此时需要调整姿态
                                if abs(angle) > 0.1:
                                    if angle > 0.1:
                                        # 左倾斜，就向右侧旋转，使用左引擎
                                        return 1
                                    else:
                                        # 右倾斜，就向左侧旋转，使用右引擎
                                        return 3
                                else:
                                    # 姿态已经调整到合适位置，完成任务
                                    return 0
                
                # 使用示例
                state = [(-0.01, 1.39), (-0.65, -0.41), (0.01,), (0.13,), (False, False)]  # 用给定的数据初始化当前的状态
                action = decide_action(state)  # 基于当前状态选择要执行的动作

                print('Action', action, 'should be taken.')
            """
            },{
                "question":
                    """
            State description: The lander is at position (-0.99, 0.43), the horizontal speed of movement is -2.02, the vertical velocity speed of movement is -0.81. The angle is 0.71 radians, and it's rotating at -0.21 radians per second. The left leg is not in contact with ground. The right leg is not in contact with ground.
            Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
            Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
                import random
                import math
                
                def decide_action(state):
                    # 获取当前状态下的关键信息
                    pos_x, pos_y = state[0]
                    speed_x, speed_y = state[1]
                    angle = state[2][0]
                    angular_vel = state[3][0]
                    left_leg_contact, right_leg_contact = state[4]
                    
                    # 设定目标区域的位置
                    target_pos = (0, 0)
                
                    # 根据目标位置与当前位置之间的关系，选择下一步的动作
                    if pos_y > target_pos[1] + 0.5 or abs(pos_x - target_pos[0]) > 0.4:
                        # 如果距离目标位置太远，就向上方和两侧移动
                        if abs(angle) > 0.4:
                            # 如果当前角度不够稳定，就继续调整角度
                            if angle > 0:
                                return 2  # 向右侧移动，使用左引擎
                            else:
                                return 4  # 向左侧移动，使用右引擎
                        else:
                            # 如果角度在可接受区间内，就开启主引擎向上移动
                            return 2
                    elif abs(speed_y) > 5 or abs(speed_x) > 1:
                        # 如果距离目标位置比较近，但速度仍然比较快，就继续调整速度和角度
                        if abs(angle) > 0.1:
                            # 如果角度不够稳定，则继续调整角度
                            if angle > 0:
                                return 2  # 向右侧移动，使用左引擎
                            else:
                                return 4  # 向左侧移动，使用右引擎
                        else:
                            # 如果速度方向偏离目标方向，则使用侧引擎调整速度
                            if speed_x < 0:
                                return 2  # 向右侧调整速度，使用左引擎
                            else:
                                return 4  # 向左侧调整速度，使用右引擎
                    else:
                        # 如果距离合适，速度较慢，就需要调整姿态使得两条腿关闭
                        if not (left_leg_contact and right_leg_contact):
                            # 如果有一个腿没有关闭，就用偏转引擎调整姿态
                            if angle > 0.1:
                                # 左倾斜，就向右侧旋转，使用左引擎
                                return 2
                            elif angle < -0.1:
                                # 右倾斜，就向左侧旋转，使用右引擎
                                return 4
                            else:
                                # 可以调整姿态
                                if left_leg_contact:
                                    # 右腿没有关闭，就向左侧旋转，使用右引擎
                                    return 4
                                else:
                                    # 左腿没有关闭，就向右侧旋转，使用左引擎
                                    return 2
                        else:
                            # 如果两条腿都关闭，则需要让LunarLander平稳着陆。首先根据竖直方向上的速度来判断
                            if abs(speed_y) > 1:
                                if speed_y < 0:
                                    # 向上移动，使用主引擎
                                    return 3
                                else:
                                    # 向下移动，则关闭引擎
                                    return 1
                            else:
                                # 竖直方向上的速度已经足够小，此时需要调整姿态
                                if abs(angle) > 0.1:
                                    if angle > 0.1:
                                        # 左倾斜，就向右侧旋转，使用左引擎
                                        return 2
                                    else:
                                        # 右倾斜，就向左侧旋转，使用右引擎
                                        return 4
                                else:
                                    # 姿态已经调整到合适位置，完成任务
                                    return 1
                
                # 使用示例
                state = [(-0.99, 0.43), (-2.02, -0.81), (0.71,), (-0.21,), (False, False)]  # 用给定的数据初始化当前的状态
                action = decide_action(state)  # 基于当前状态选择要执行的动作

                print('Action', action, 'should be taken.')
            """
            }
        ]


class CONSISTENCY:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [{
                "question":
                    """
            State description: The lander is at position (-0.01, 1.39), the horizontal speed of movement is -0.65, the vertical velocity speed of movement is -0.41. The angle is 0.01 radians, and it's rotating at 0.13 radians per second. The left leg is not in contact with ground. The right leg is not in contact with ground.
            Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
            Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            According to the current state description, the lander is moving to the left at a high horizontal velocity and needs to reduce its horizontal velocity to land safely. However, at the same time, the lander is landing at a higher velocity of 0.41. Therefore, we can choose operation 3 (fire the main engine) to reduce the descent velocity. Therefore, the final answer is fire the main engine (operation 3).
            """
            },
            {
                "question":
                    """
            State description: The lander is at position (-0.99, 0.43), the horizontal speed of movement is -2.02, the vertical velocity speed of movement is -0.81. The angle is 0.71 radians, and it's rotating at -0.21 radians per second. The left leg is not in contact with ground. The right leg is not in contact with ground.
            Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
            Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            According to the current state description, the lander is moving to the left at a high horizontal velocity and needs to reduce its horizontal velocity to land safely. However, at the same time, the lander is landing at a higher velocity of 0.81. Therefore, we can choose operation 3 (fire the main engine) to reduce the descent velocity. Therefore, the final answer is fire the main engine (operation 3).
            """
            }]


class SELFASK:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [{
                "question":
                    """
            State description: The lander is at position (-0.01, 1.39), the horizontal speed of movement is -0.65, the vertical velocity speed of movement is -0.41. The angle is 0.01 radians, and it's rotating at 0.13 radians per second. The left leg is not in contact with ground. The right leg is not in contact with ground.
            Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
            Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            Are follow up questions needed here: Yes.
            Follow up: Where is the position of the lander now?
            Intermediate answer: The position of the lander is at position (-0.01,1.39), the horizontal coordinate is slightly shifted to the left by 0.01 from the center, and the vertical coordinate is 1.39 from the ground, which is farther away.
            Follow up: What is the lateral velocity of the lander?
            Intermediate answer: The lateral velocity of the lander is 0.65, moving to the left.
            Follow up: What is the descent velocity of the lander?
            Intermediate answer: The lander's descent velocity is 0.41 which is larger.
            Follow up: What is the angle and angular velocity of the lander?
            Intermediate answer: The lander rotated 0.01 radians counterclockwise and at an angular velocity of 0.13 radians per second, the lander was relatively balanced.
            Follow up: Are the lander's left and right legs in contact with the ground?
            Intermediate answer: Neither the left nor right leg of the lander made contact with the ground..
            Follow up: Which of the three goals of maintaining a smooth lander attitude, moving to the center, and adjusting the rate of descent is more important in the current state??
            Intermediate answer: Adjusting the lander descent rate is more important in the current state.
            So the final answer is: Fire main engine and make lander move to up (Action 3).
            """
            },
            {
                "question":
                    """
            State description: The lander is at position (-0.99, 0.43), the horizontal speed of movement is -2.02, the vertical velocity speed of movement is -0.81. The angle is 0.71 radians, and it's rotating at -0.21 radians per second. The left leg is not in contact with ground. The right leg is not in contact with ground.
            Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
            Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
            """,
                "answer":
                    """
            Are follow up questions needed here: Yes.
            Follow up: Where is the position of the lander now?
            Intermediate answer: The position of the lander is at position (-0.99, 0.43), the horizontal coordinate is shifted to the left by 0.99 from the center, and the vertical coordinate is 0.43 from the ground, which is close to the ground.
            Follow up: What is the lateral velocity of the lander?
            Intermediate answer: The lateral velocity of the lander is 2.02, moving to the left.Looks like the lander has a little too much lateral velocity.
            Follow up: What is the descent velocity of the lander?
            Intermediate answer: The lander's descent velocity is 0.81 which is larger.
            Follow up: What is the angle and angular velocity of the lander?
            Intermediate answer: The lander rotated counterclockwise by 0.71 radians and rotated clockwise at an angular velocity of 0.21 radians per second.
            Follow up: Are the lander's left and right legs in contact with the ground?
            Intermediate answer: Neither the left nor right leg of the lander made contact with the ground..
            Follow up: Which of the three goals of maintaining a smooth lander attitude, moving to the center, and adjusting the rate of descent is more important in the current state?
            Intermediate answer: Adjusting the lander descent rate is more important in the current state.
            So the final answer is: Fire main engine and make lander move to up (Action 3).
            """
            }]


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
                State description: The lander is at position (-0.01, 1.39), the horizontal speed of movement is -0.65, the vertical velocity speed of movement is -0.41. The angle is 0.01 radians, and it's rotating at 0.13 radians per second. The left leg is not in contact with ground. The right leg is not in contact with ground.
                Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
                Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                Your memory for the task below:
                Trial 0:
                I was not able to land the lander on the landing pad. I should have tried to balance the engine to slow down my descent and land gently. I will try to balance the engine to slow down my descent and land gently in the next trial.<|im_end|>
                Trial 1:
                In this environment, my plan was to balance the engine to slow down my descent and land gently. However, I was not able to land the lander on the landing pad. I should have tried to balance the engine to slow down my descent and land gently. I will try to balance the engine to slow down my descent and land gently in the next trial.<|im_end|>
                Trial 2:
                I will try to balance the engine to slow down my descent and land gently.<|im_end|>
                    """,
                "answer":
                    """
                Based on the current game state and memories of the task, the optimal action for the player to take would be to fire main engine (action 3) to reduce the descent velocity of the spacecraft. Therefore, the optimal action to take now is to fire main engine (action 3).
                    """
            },
            {
                "question":
                    """
                State description: The lander is at position (0.31, 0.04), the horizontal speed of movement is -0.21, the vertical velocity speed of movement is -0.09. The angle is 0.24 radians, and it's rotating at 0.17 radians per second. The left leg is not in contact with ground. The right leg is in contact with ground.
                Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
                Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                Your memory for the task below:
                Trial 0:
                In this environment, my plan was to balance the engine to slow down my descent and land gently. However, I was not able to land the lander on the landing pad. I should have tried to balance the engine to slow down my descent and land gently. I will try to balance the engine to slow down my descent and land gently in the next trial.<|im_end|>
                Trial 1:
                I will try to balance the engine to slow down my descent and land gently.<|im_end|>
                Trial 2:
                I will try to balance the engine to slow down my descent and land gently.<|im_end|>
                    """,
                "answer":
                    """
                Based on the current game state and memories of the task, the optimal action for the player to take would be to fire main engine (action 3) to reduce the descent velocity of the spacecraft. Therefore, the optimal action to take now is to fire main engine (action 3).
                    """
            },
        ]

class EGG:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: The lander is at position (-0.01, 1.39), the horizontal speed of movement is -0.65, the vertical velocity speed of movement is -0.41. The angle is 0.01 radians, and it's rotating at 0.13 radians per second. The left leg is not in contact with ground. The right leg is not in contact with ground.
                Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
                Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                The insights of the game are listed below: The key information that can be exploited to improve the player's performance includes taking into account the lander's movement and adjusting the thrust accordingly to stabilize its descent, considering the angle and rotation of the lander to ensure a gentle landing, and fine-tuning the policy to optimize the thrust and angle adjustments for a smoother landing. Additionally, the player should avoid constantly applying thrust to the lander as it may not be effective in successfully landing the lander on the pad.
                The suggestions are listed below:
                1. For exploration in the next episode, the player should focus on gathering more information about the lander's movement and behavior during descent. This can be done by varying the thrust and angle adjustments to see how the lander responds, and observing any patterns or trends in its movement. The player can also try different starting positions and initial forces to see how they affect the lander's trajectory. 
                2. To improve the policy for higher performance in the next episode, the player should focus on fine-tuning the thrust and angle adjustments to optimize the lander's descent and landing. This can be done by analyzing the data gathered from exploration and adjusting the policy accordingly. The player should also pay attention to the lander's rotation and angle to ensure a gentle landing on the pad. 
                3. The player should weigh exploration and exploitation equally in the next episode, as both are important for improving the policy and achieving a successful landing. The player should continue to gather information through exploration while also using that information to make informed decisions during exploitation.
                    """,
                "answer":
                    """
                Based on the current game state, the insights and the suggestions, the optimal action for the player to take would be to fire main engine (action 3) to reduce the descent velocity of the spacecraft. Therefore, the optimal action to take now is to fire main engine (action 3).
                    """
            },
            {
                "question":
                    """
                State description: The lander is at position (0.31, 0.04), the horizontal speed of movement is -0.21, the vertical velocity speed of movement is -0.09. The angle is 0.24 radians, and it's rotating at 0.17 radians per second. The left leg is not in contact with ground. The right leg is in contact with ground.
                Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
                Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                The insights of the game are listed below: The key information that can be exploited to improve the player's performance includes taking into account the lander's movement and adjusting the thrust accordingly to stabilize its descent, considering the angle and rotation of the lander to ensure a gentle landing, and adjusting the thrust to ensure a gentle landing when the lander makes contact with the ground. Additionally, fine-tuning the policy to optimize the thrust and angle adjustments for a smoother landing can further improve performance.
                The suggestions are listed below:
                1. Exploration: 
                - The player should explore the effect of adjusting the thrust and angle of the lander during descent to ensure a gentle landing on the pad. 
                - To make the exploration, the player can try different combinations of thrust and angle adjustments during descent and observe the effect on the lander's movement and performance score.
                2. Exploitation: 
                - The player should improve the policy by taking into account the contact with the ground and adjusting the thrust accordingly to ensure a gentle landing. 
                - Additionally, the policy should also take into account the angle and rotation of the lander to ensure that it lands upright on the pad. 
                - To improve the policy, the player can use the information obtained from the previous episodes and adjust the thrust and angle accordingly during descent.
                3. Trade-off: 
                - The player should focus more on exploitation in the next episode as they have already explored different thrust and angle adjustments in the previous episodes. 
                - However, the player should still allocate some time for exploration to fine-tune the policy and ensure a successful landing on the pad. 
                - A good trade-off would be to allocate seventy percent of the time for exploitation and thirty percent of the time for exploration.
                    """,
                "answer":
                    """
                Based on the current game state, the insights and the suggestions, the optimal action for the player to take would be to fire main engine (action 3) to reduce the descent velocity of the spacecraft. Therefore, the optimal action to take now is to fire main engine (action 3).
                    """
            },
        ]

class EGGWithoutInsights:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: The lander is at position (-0.01, 1.39), the horizontal speed of movement is -0.65, the vertical velocity speed of movement is -0.41. The angle is 0.01 radians, and it's rotating at 0.13 radians per second. The left leg is not in contact with ground. The right leg is not in contact with ground.
                Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
                Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                The suggestions are listed below:
                1. For exploration in the next episode, the player should focus on gathering more information about the lander's movement and behavior during descent. This can be done by varying the thrust and angle adjustments to see how the lander responds, and observing any patterns or trends in its movement. The player can also try different starting positions and initial forces to see how they affect the lander's trajectory. 
                2. To improve the policy for higher performance in the next episode, the player should focus on fine-tuning the thrust and angle adjustments to optimize the lander's descent and landing. This can be done by analyzing the data gathered from exploration and adjusting the policy accordingly. The player should also pay attention to the lander's rotation and angle to ensure a gentle landing on the pad. 
                3. The player should weigh exploration and exploitation equally in the next episode, as both are important for improving the policy and achieving a successful landing. The player should continue to gather information through exploration while also using that information to make informed decisions during exploitation.
                    """,
                "answer":
                    """
                Based on the current game state and the suggestions, the optimal action for the player to take would be to fire main engine (action 3) to reduce the descent velocity of the spacecraft. Therefore, the optimal action to take now is to fire main engine (action 3).
                    """
            },
            {
                "question":
                    """
                State description: The lander is at position (0.31, 0.04), the horizontal speed of movement is -0.21, the vertical velocity speed of movement is -0.09. The angle is 0.24 radians, and it's rotating at 0.17 radians per second. The left leg is not in contact with ground. The right leg is in contact with ground.
                Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
                Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                The suggestions are listed below:
                1. Exploration: 
                - The player should explore the effect of adjusting the thrust and angle of the lander during descent to ensure a gentle landing on the pad. 
                - To make the exploration, the player can try different combinations of thrust and angle adjustments during descent and observe the effect on the lander's movement and performance score.
                2. Exploitation: 
                - The player should improve the policy by taking into account the contact with the ground and adjusting the thrust accordingly to ensure a gentle landing. 
                - Additionally, the policy should also take into account the angle and rotation of the lander to ensure that it lands upright on the pad. 
                - To improve the policy, the player can use the information obtained from the previous episodes and adjust the thrust and angle accordingly during descent.
                3. Trade-off: 
                - The player should focus more on exploitation in the next episode as they have already explored different thrust and angle adjustments in the previous episodes. 
                - However, the player should still allocate some time for exploration to fine-tune the policy and ensure a successful landing on the pad. 
                - A good trade-off would be to allocate seventy percent of the time for exploitation and thirty percent of the time for exploration.
                    """,
                "answer":
                    """
                Based on the current game state and the suggestions, the optimal action for the player to take would be to fire main engine (action 3) to reduce the descent velocity of the spacecraft. Therefore, the optimal action to take now is to fire main engine (action 3).
                    """
            },
        ]

class EGGWithoutSuggestions:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: The lander is at position (-0.01, 1.39), the horizontal speed of movement is -0.65, the vertical velocity speed of movement is -0.41. The angle is 0.01 radians, and it's rotating at 0.13 radians per second. The left leg is not in contact with ground. The right leg is not in contact with ground.
                Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
                Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                The insights of the game are listed below: The key information that can be exploited to improve the player's performance includes taking into account the lander's movement and adjusting the thrust accordingly to stabilize its descent, considering the angle and rotation of the lander to ensure a gentle landing, and fine-tuning the policy to optimize the thrust and angle adjustments for a smoother landing. Additionally, the player should avoid constantly applying thrust to the lander as it may not be effective in successfully landing the lander on the pad.
                    """,
                "answer":
                    """
                Based on the current game state and the insights, the optimal action for the player to take would be to fire main engine (action 3) to reduce the descent velocity of the spacecraft. Therefore, the optimal action to take now is to fire main engine (action 3).
                    """
            },
            {
                "question":
                    """
                State description: The lander is at position (0.31, 0.04), the horizontal speed of movement is -0.21, the vertical velocity speed of movement is -0.09. The angle is 0.24 radians, and it's rotating at 0.17 radians per second. The left leg is not in contact with ground. The right leg is in contact with ground.
                Goal description: The goal is to successfully land the lander on the landing pad which is at position (0, 0) with a vertical velocity close to 0, and make sure all two legs are up and the lander is balanced.
                Action description: Please choose an action. Type '1' to do noting, '2' to fire left engine and make lander move to right, '3' to fire main engine and make lander move to up, or '4' to fire right engine and make lander move to left. Ensure you only provide the action number from the valid action list, i.e., [1, 2, 3, 4].
                The insights of the game are listed below: The key information that can be exploited to improve the player's performance includes taking into account the lander's movement and adjusting the thrust accordingly to stabilize its descent, considering the angle and rotation of the lander to ensure a gentle landing, and adjusting the thrust to ensure a gentle landing when the lander makes contact with the ground. Additionally, fine-tuning the policy to optimize the thrust and angle adjustments for a smoother landing can further improve performance.
                    """,
                "answer":
                    """
                Based on the current game state and the insights, the optimal action for the player to take would be to fire main engine (action 3) to reduce the descent velocity of the spacecraft. Therefore, the optimal action to take now is to fire main engine (action 3).
                    """
            },
        ]