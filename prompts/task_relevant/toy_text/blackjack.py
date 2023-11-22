class ACT:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: The player's current sum is 12, the dealer is showing 6, and the player has a usable ace: no.
                Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
                Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
                    """,
                "answer":
                    """The final answer is: stick (stop receiving cards) (Action 1)."""
            },
            {
                "question":
                    """
                State description: Current Game State: The player's current sum is 17, the dealer is showing 10, and the player has a usable ace: no.
                Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
                Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
                    """,
                "answer":
                    """The final answer is: stick (stop receiving cards) (Action 1)."""
            }
        ]


class COT:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: The player's current sum is 12, the dealer is showing 6, and the player has a usable ace: no.
                Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
                Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
                    """,
                "answer":
                    """In the specific case where the player's hand is 12 and the dealer's visible card is 6, according to the game rules, the dealer must have at least 17 points in their hand to stop taking another card. 
                    If the dealer's card value is relatively small, the probability of the dealer taking another card is relatively high. 
                    If the player takes another card in this situation, there is a risk of exceeding 21 points, so the optimal strategy is to stick (stop receiving cards).
                    So the final answer is: stick (stop receiving cards) (Action 1)."""
            },
            {
                "question":
                    """
                State description: Current Game State: The player's current sum is 17, the dealer is showing 10, and the player has a usable ace: no.
                Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
                Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
                    """,
                "answer":
                    """The player's current sum of cards is 17, while the dealer is showing a 10, and the player does not have a usable ace. 
                    The objective is to have a card sum closer to 21, without exceeding that value, to beat the dealer.
                    Since the player's sum is 17 and there is a risk of going over 21 if the player hits, it might be wiser to stick with the current hand and not take an additional card to avoid the risk of busting. 
                    So the final answer is: stick (stop receiving cards) (Action 1)."""
            }
        ]


class PAL:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: The player's current sum is 12, the dealer is showing 6, and the player has a usable ace: no.
                Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
                Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
                    """,
                "answer":
                    """
                def should_hit(player_score, dealer_score, usable_ace):
                    if usable_ace:
                        if player_score >= 13 and player_score <= 17:
                            return 2
                        if player_score == 18:
                            if dealer_score >= 2 and dealer_score <= 8:
                                return 1
                            else:
                                return 2
                        if player_score >= 19:
                            return 1
                        return 2
                    else:
                        if player_score <= 11:
                            return 2
                        if player_score == 12: 
                            if (dealer_score >= 4 and dealer_score <= 6):
                                return 1
                            else:
                                return 2
                        if player_score >= 13 and player_score <= 16:
                            if dealer_score >= 2 and dealer_score <= 6:
                                return 1
                            else:
                                return 2
                        if player_score >= 17:
                            return 1
                    return 1
                player_sum = 12
                dealer_card = 6
                player_usable_ace = False

                action = should_hit(player_sum, dealer_card, player_usable_ace)
                action_description = dict()
                action_description[1] =  "Stick (stop receiving cards)"
                action_description[2] =  "Hit (add a card)"

                print("The optimal action is: " + str(action_description[action]) + " (Action " + str(action) + ")")
                The optimal action is: Stick (stop receiving cards) (Action 1)
           """
            },{
                "question":
                    """
                State description: Current Game State: The player's current sum is 17, the dealer is showing 10, and the player has a usable ace: no.
                Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
                Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
                    """,
                "answer":
                    """
                def should_hit(player_score, dealer_score, usable_ace):
                    if usable_ace:
                        if player_score >= 13 and player_score <= 17:
                            return 2
                        if player_score == 18:
                            if dealer_score >= 2 and dealer_score <= 8:
                                return 1
                            else:
                                return 2
                        if player_score >= 19:
                            return 1
                        return 2
                    else:
                        if player_score <= 11:
                            return 2
                        if player_score == 12: 
                            if (dealer_score >= 4 and dealer_score <= 6):
                                return 1
                            else:
                                return 2
                        if player_score >= 13 and player_score <= 16:
                            if dealer_score >= 2 and dealer_score <= 6:
                                return 1
                            else:
                                return 2
                        if player_score >= 17:
                            return 1
                    return 1
                player_sum = 17
                dealer_card = 10
                player_usable_ace = False

                action = should_hit(player_sum, dealer_card, player_usable_ace)
                action_description = dict()
                action_description[1] =  "Stick (stop receiving cards)"
                action_description[2] =  "Hit (add a card)"

                print("The optimal action is: " + str(action_description[action]) + " (Action " + str(action) + ")")
                The optimal action is: Stick (stop receiving cards) (Action 1)
           """
            },
        ]


class CONSISTENCY:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: The player's current sum is 12, the dealer is showing 6, and the player has a usable ace: no.
                Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
                Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
                    """,
                "answer":
                    """TIn the specific case where the player's hand is 12 and the dealer's visible card is 6, according to the game rules, the dealer must have at least 17 points in their hand to stop taking another card. 
                    If the dealer's card value is relatively small, the probability of the dealer taking another card is relatively high. 
                    If the player takes another card in this situation, there is a risk of exceeding 21 points, so the optimal strategy is to stick (stop receiving cards).
                    So the final answer is: stick (stop receiving cards) (Action 1)."""
            },
            {
                "question":
                    """
                State description: Current Game State: The player's current sum is 17, the dealer is showing 10, and the player has a usable ace: no.
                Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
                Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
                    """,
                "answer":
                    """The player's current sum of cards is 17, while the dealer is showing a 10, and the player does not have a usable ace. 
                    The objective is to have a card sum closer to 21, without exceeding that value, to beat the dealer.
                    Since the player's sum is 17 and there is a risk of going over 21 if the player hits, it might be wiser to stick with the current hand and not take an additional card to avoid the risk of busting. 
                    So the final answer is: stick (stop receiving cards) (Action 1)."""
            }
        ]


class SELFASK:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
            State description: Current Game State: The player's current sum is 12, the dealer is showing 6, and the player has a usable ace: no.
            Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
            Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
            """,
                "answer":
                    """
            Are follow up questions needed here: Yes.
            Follow up: What is the player's current sum?
            Intermediate answer: The player's current sum is 12.
            Follow up: What card is the dealer showing?
            Intermediate answer: The dealer is showing a 6.
            Follow up: Does the player have a usable ace?
            Intermediate answer: No, the player does not have a usable ace.
            Follow up: What is the goal of the game?
            Intermediate answer: The goal of the game is to have a higher sum of cards than the dealer without going over 21.
            Follow up: What are the possible actions for the player?
            Intermediate answer: The player can choose to stick (stop receiving cards) or hit (add a card).
            Follow up: What is the optimal action for the player in its current state?
            Intermediate answer: Since the player's current sum is 12 and the dealer is showing a 6, according to the game rules, the dealer must have at least 17 points in their hand to stop taking another card. Because the dealer's total is relatively small, the dealer faces an even greater risk of exceeding 21 points. Considering this, the optimal action would be to stick (stop receiving cards). 
            So the final answer is: stick (stop receiving cards) (Action 1).
            """
            },
            {
                "question":
                    """
            State description: Current Game State: The player's current sum is 17, the dealer is showing 10, and the player has a usable ace: no.
            Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
            Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
            """,
                "answer":
                    """
            Are follow up questions needed here: Yes.
            Follow up: What is the player's current sum?
            Intermediate answer: The player's current sum is 17.
            Follow up: What card is the dealer showing?
            Intermediate answer: The dealer is showing a 10.
            Follow up: Does the player have a usable ace?
            Intermediate answer: No, the player does not have a usable ace.
            Follow up: What is the goal of the game?
            Intermediate answer: The goal of the game is to have a higher sum of cards than the dealer without going over 21.
            Follow up: What are the possible actions for the player?
            Intermediate answer: The player can choose to stick (stop receiving cards) or hit (add a card).
            Follow up: What is the optimal action for the player in its current state?
            Intermediate answer: Since the player's current sum is 17 and the dealer is showing a 10, the optimal action would be to stick (stop receiving cards). The player has a relatively high sum and the risk of going over 21 is significant if another card is added.
            So the final answer is: stick (stop receiving cards) (Action 1).
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
                State description: Current Game State: The player's current sum is 11, the dealer is showing 1, and the player has a usable ace: no.
                Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
                Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
                Your memory for the task below:
                Trial 0:
                In the game of Blackjack, the main aim is to obtain a higher card sum than the dealer, but not higher than 21. Face cards count as 10, numerical cards hold their value, and aces can count either as 1 or 11. The game starts with the dealer having one face-up and one face-down card, while the player has two face-up cards. The player can either choose to 'hit' (add a card) or 'stick' (stop receiving cards). The game ends when the player or the dealer busts or when both the player and dealer are finished drawing cards. In the previous trial, I did not follow the rules of Blackjack. I should have added a card to my hand instead of choosing to stick. In the next trial, I will add a card to my hand if my current sum is less than 17. If my current sum is greater than or equal to 17, I will choose to stick.<|im_end|>
                Trial 1:
                In the current game state, my current sum is 15 and the dealer is showing 9. I should add a card to my hand because my current sum is less than 17. I will choose to hit.<|im_end|>
                Trial 2:
                In the game of Blackjack, the main aim is to obtain a higher card sum than the dealer, but not higher than 21. Face cards count as 10, numerical cards hold their value, and aces can count either as 1 or 11. The game starts with the dealer having one face-up and one face-down card, while the player has two face-up cards. The player can either choose to 'hit' (add a card) or 'stick' (stop receiving cards). The game ends when the player or the dealer busts or when both the player and dealer are finished drawing cards. In the previous trials, I did not follow the rules of Blackjack. I should have added a card to my hand instead of choosing to stick. In the next trial, I will add a card to my hand if my current sum is less than 17. If my current sum is greater than or equal to 17, I will choose to stick.<|im_end|>
                    """,
                "answer":
                    """
                The optimal action is: 2.
                    """
            },
            {
                "question":
                    """
                State description: Current Game State: The player's current sum is 18, the dealer is showing 9, and the player has a usable ace: no.
                Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
                Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
                Your memory for the task below:
                Trial 0:
                In the game of Blackjack, the main aim is to obtain a higher card sum than the dealer, but not higher than 21. Face cards count as 10, numerical cards hold their value, and aces can count either as 1 or 11. The game starts with the dealer having one face-up and one face-down card, while the player has two face-up cards. The player can either choose to 'hit' (add a card) or 'stick' (stop receiving cards). The game ends when the player or the dealer busts or when both the player and dealer are finished drawing cards. In the previous trial, I did not follow the rules of Blackjack. I should have added a card to my hand instead of choosing to stick. In the next trial, I will add a card to my hand if my current sum is less than 17. If my current sum is greater than or equal to 17, I will choose to stick.<|im_end|>
                Trial 1:
                In the game of Blackjack, the main aim is to obtain a higher card sum than the dealer, but not higher than 21. Face cards count as 10, numerical cards hold their value, and aces can count either as 1 or 11. The game starts with the dealer having one face-up and one face-down card, while the player has two face-up cards. The player can either choose to 'hit' (add a card) or 'stick' (stop receiving cards). The game ends when the player or the dealer busts or when both the player and dealer are finished drawing cards. In the previous trial, I did not follow the rules of Blackjack. I should have added a card to my hand instead of choosing to stick. In the next trial, I will add a card to my hand if my current sum is less than 17. If my current sum is greater than or equal to 17, I will choose to stick.<|im_end|>
                Trial 2:
                In the current game state, my current sum is 15 and the dealer is showing 9. I should add a card to my hand because my current sum is less than 17. I will choose to hit.
                    """,
                "answer":
                    """The optimal action is: 1."""
            }
        ]

class EGG:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: The player's current sum is 6, the dealer is showing 7, and the player has a usable ace: no.
                Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
                Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
                The insights of the game are listed below: The key information that can be exploited to improve the performance of the player is the presence of a usable ace in their hand. This information can be used to inform the player's decision-making process and potentially improve their performance by allowing them to make more informed decisions about whether to hit or stick based on the value of their hand. By taking into account the value of the ace, the player can potentially increase their chances of winning the hand.
                The suggestions are listed below:
                1. For exploration in the next episode, the player should try to observe the dealer's face-up card and use that information to inform their decision-making process. They can do this by hitting until they have a hand value of at least 12, and then observing the dealer's card before deciding whether to hit or stick. This will help the player make more informed decisions and potentially increase their chances of winning.
                2. To improve the policy and gain a higher performance in the next episode, the player should focus on using their usable ace to their advantage. They should aim to use the ace as 11 when their hand value is low (e.g. less than 12) and as 1 when their hand value is high (e.g. more than 17). This will help the player avoid busting and increase their chances of getting closer to 21.
                3. The player should weight exploration and exploitation equally in the next episode. While it is important to explore and gather new information, it is also important to use that information to improve performance. By balancing exploration and exploitation, the player can make more informed decisions and potentially increase their chances of winning.
                    """,
                "answer":
                    """
                Based on the current game state, the insights and the suggestions, the player should hit (add a card) as their current sum is very low and they have no usable ace to use to their advantage. 
                The goal is to get closer to 21 without going over, and hitting will increase the player's chances of achieving this goal. 
                Therefore, the optimal action for the player is to choose action number 2 to hit. 
                    """
            },{
                "question":
                    """
                State description: Current Game State: The player's current sum is 20, the dealer is showing 4, and the player has a usable ace: no.
                Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
                Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
                The insights of the game are listed below: The key information that can be exploited to improve the performance of the player includes the presence of a usable ace, the player's current hand sum, the dealer's face-up card, and the likelihood of the dealer having a higher hand. By taking into account these factors, the player can make more informed decisions on whether to hit or stick, potentially increasing their chances of winning.
                The suggestions are listed below:
                1. Exploration: The player should explore the value of their usable ace in different scenarios. They can try using the ace as 1 or 11 and observe the outcome. To make the exploration, the player can randomly choose to use the ace as 1 or 11 in different game states and record the results.
                2. Exploitation: The player should improve their policy by considering the dealer's face-up card and the likelihood of the dealer having a higher hand. They can also use the information from the previous trajectories to make more informed decisions. For example, if the player has a low hand value and the dealer has a high face-up card, the player may choose to hit to improve their hand. On the other hand, if the player has a high hand value and the dealer has a low face-up card, the player may choose to stick to avoid going over 21.
                3. Weighting: The player should balance exploration and exploitation by allocating more time to exploitation. Since the player only has two episodes left, they should focus on exploiting the information they have gathered so far to increase their chances of winning. However, they should also continue to explore the value of their usable ace in different scenarios to potentially improve their policy in future games.
                    """,
                "answer":
                    """Based on the current game state, the insights and the suggestions, The optimal action is: 1."""
            }
        ]

class EGGWithoutInsights:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: The player's current sum is 6, the dealer is showing 7, and the player has a usable ace: no.
                Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
                Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
                The suggestions are listed below:
                1. For exploration in the next episode, the player should try to observe the dealer's face-up card and use that information to inform their decision-making process. They can do this by hitting until they have a hand value of at least 12, and then observing the dealer's card before deciding whether to hit or stick. This will help the player make more informed decisions and potentially increase their chances of winning.
                2. To improve the policy and gain a higher performance in the next episode, the player should focus on using their usable ace to their advantage. They should aim to use the ace as 11 when their hand value is low (e.g. less than 12) and as 1 when their hand value is high (e.g. more than 17). This will help the player avoid busting and increase their chances of getting closer to 21.
                3. The player should weight exploration and exploitation equally in the next episode. While it is important to explore and gather new information, it is also important to use that information to improve performance. By balancing exploration and exploitation, the player can make more informed decisions and potentially increase their chances of winning.
                    """,
                "answer":
                    """
                Based on the current game state and the suggestions, the player should hit (add a card) as their current sum is very low and they have no usable ace to use to their advantage. 
                The goal is to get closer to 21 without going over, and hitting will increase the player's chances of achieving this goal. 
                Therefore, the optimal action for the player is to choose action number 2 to hit. 
                    """
            },{
                "question":
                    """
                State description: Current Game State: The player's current sum is 20, the dealer is showing 4, and the player has a usable ace: no.
                Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
                Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
                The suggestions are listed below:
                1. Exploration: The player should explore the value of their usable ace in different scenarios. They can try using the ace as 1 or 11 and observe the outcome. To make the exploration, the player can randomly choose to use the ace as 1 or 11 in different game states and record the results.
                2. Exploitation: The player should improve their policy by considering the dealer's face-up card and the likelihood of the dealer having a higher hand. They can also use the information from the previous trajectories to make more informed decisions. For example, if the player has a low hand value and the dealer has a high face-up card, the player may choose to hit to improve their hand. On the other hand, if the player has a high hand value and the dealer has a low face-up card, the player may choose to stick to avoid going over 21.
                3. Weighting: The player should balance exploration and exploitation by allocating more time to exploitation. Since the player only has two episodes left, they should focus on exploiting the information they have gathered so far to increase their chances of winning. However, they should also continue to explore the value of their usable ace in different scenarios to potentially improve their policy in future games.
                    """,
                "answer":
                    """Based on the current game state and the suggestions, The optimal action is: 1."""
            }
        ]

class EGGWithoutSuggestions:
    def __init__(self):
        self.PERCEPTRON_BASIC_FS_EXAMPLES = [
            {
                "question":
                    """
                State description: Current Game State: The player's current sum is 6, the dealer is showing 7, and the player has a usable ace: no.
                Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
                Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
                The insights of the game are listed below: The key information that can be exploited to improve the performance of the player is the presence of a usable ace in their hand. This information can be used to inform the player's decision-making process and potentially improve their performance by allowing them to make more informed decisions about whether to hit or stick based on the value of their hand. By taking into account the value of the ace, the player can potentially increase their chances of winning the hand.
                    """,
                "answer":
                    """
                Based on the current game state and the insights, the player should hit (add a card) as their current sum is very low and they have no usable ace to use to their advantage. 
                The goal is to get closer to 21 without going over, and hitting will increase the player's chances of achieving this goal. 
                Therefore, the optimal action for the player is to choose action number 2 to hit. 
                    """
            },{
                "question":
                    """
                State description: Current Game State: The player's current sum is 20, the dealer is showing 4, and the player has a usable ace: no.
                Goal description: The goal is to beat the dealer by obtaining cards that sum to closer to 21, without going over 21.
                Action description: Your Next Move: \n Please choose an action. Type '1' to stick (stop receiving cards) or '2' to hit (add a card). Ensure you only provide the action number from the valid action list, i.e., [1, 2].
                The insights of the game are listed below: The key information that can be exploited to improve the performance of the player includes the presence of a usable ace, the player's current hand sum, the dealer's face-up card, and the likelihood of the dealer having a higher hand. By taking into account these factors, the player can make more informed decisions on whether to hit or stick, potentially increasing their chances of winning.
                    """,
                "answer":
                    """Based on the current game state and the insights, The optimal action is: 1."""
            }
        ]