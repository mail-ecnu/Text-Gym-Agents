class ACT:
    def __init__(self):
        self.TASK_IRRELEVANT_PROMPTS = []

class EXE:
    def __init__(self):
        self.TASK_IRRELEVANT_PROMPTS = []

class COT:
    def __init__(self):
        self.TASK_IRRELEVANT_PROMPTS = [{
            "question":
                "Could Brooke Shields succeed at University of Pennsylvania?",
            "answer":
                """
                Brooke Shields went to Princeton University. Princeton University is about as academically rigorous as the
                University of Pennsylvania. Thus, Brooke Shields could also succeed at the University of Pennsylvania. So the
                answer is yes.
                """
        },{
            "question":
                    "Olivia has $23. She bought five bagels for $3 each. How much money does she have left?",
            "answer":
                """
                Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 15 dollars. So she has 23 - 15 dollars left. 23 - 15 is 8. The answer is 8.
                """
        }]


class PAL:
    def __init__(self):
        self.TASK_IRRELEVANT_PROMPTS = [{
            "question":
                "Olivia has $23. She bought five bagels for $3 each. How much money does she have left?",
            "answer":
                """
                ```
                money_initial = 23
                bagels = 5
                bagel_cost = 3
                money_spent = bagels * bagel_cost
                money_left = money_initial - money_spent
                answer = money_left
                print("The final answer is :", answer)
                # The final answer is : 8
                ```
                """
            },{
            "question":
                " Four years ago, Kody was only half as old as Mohamed. If Mohamed is currently twice 30 years old, how old is Kody?",
            "answer":
                """
                ```
                # Four years ago, Kody was only half as old as Mohamed. If Mohamed is currently twice
                30 years old, how old is Kody?
                # How old was Mohamed four years ago?
                mohamed_age_current = 30 * 2
                mohamed_age_4_years_ago = mohamed_age_current - 4
                # Final Question: How old is Kody?
                kody_age_4_years_ago = mohamed_age_4_years_ago / 2
                kody_age_current = kody_age_4_years_ago + 4
                answer = kody_age_current
                print("The final answer is :", answer)
                # The final answer is : 32
                ```
                """
        }]


class CONSISTENCY:
    def __init__(self):
        self.TASK_IRRELEVANT_PROMPTS = [{
            "question":
                "Could Brooke Shields succeed at University of Pennsylvania?",
            "answer":
                """
                Brooke Shields went to Princeton University. Princeton University is about as academically rigorous as the
                University of Pennsylvania. Thus, Brooke Shields could also succeed at the University of Pennsylvania. So the
                answer is yes.
                """
        },{
            "question":
                    "Olivia has $23. She bought five bagels for $3 each. How much money does she have left?",
                "answer":
                    """
                    Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 15 dollars. So she has 23 - 15 dollars left. 23 - 15 is 8. The answer is 8.
                    """
        }]


class SELFASK:
    def __init__(self):
        self.TASK_IRRELEVANT_PROMPTS = [
            {
                "question":
                    """
                The birth country of Jayantha Ketagoda left the British Empire when?
                    """,
                "answer":
                    """
                Are follow up questions needed here: Yes.
                Follow up: What is the birth country of Jayantha Ketagoda?
                Intermediate answer: Sri Lanka.
                Follow up: When did Sri Lanka leave the British Empire?
                Intermediate answer: Sri Lanka left the British Empire on February 4, 1948.
                So the final answer is: February 4, 1948.
                    """
            },
            {
                "question":
                    """
                When does monsoon season end in the state the area code 575 is located?
                    """,
                "answer":
                    """
                Are follow up questions needed here: Yes.
                Follow up: Which state is the area code 575 located in?
                Intermediate answer: The area code 575 is located in New Mexico.
                Follow up: When does monsoon season end in New Mexico?
                Intermediate answer: Monsoon season in New Mexico typically ends in mid-September.
                So the final answer is: mid-September.

                    """
        }]


class SPP:
    def __init__(self):
        self.TASK_IRRELEVANT_PROMPTS = [
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
            }]
        
class REFLEXION:
    def __init__(self):
        self.TASK_IRRELEVANT_PROMPTS = [
            {
                "question":
                    """
        You are in the middle of a room. Looking quickly around you, you see a cabinet 10, a cabinet 9, a cabinet 8, a cabinet 7, a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 2, a countertop 1, a diningtable 2, a diningtable 1, a drawer 3, a drawer 2, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
        Your task is to: heat some mug and put it in coffeemachine.
                    """,
                "answer":
                     """
                > think: To solve the task, I need to find and take a mug, then heat it with stoveburner, then put it in coffeemachine.
                Ok.
                > look
                You are in the middle of a room. Looking quickly around you, you see nothing.
                > think: First I need to find a mug. A mug is more likely to appear in countertop (1-2), diningtable (1-2), drawer (1-3), fridge (1), sinkbasin (1), stoveburner (1-4), toaster (1). I can check one by one, starting with countertop 1.
                Ok.
                > look
                You are in the middle of a room. Looking quickly around you, you see nothing.
                > go to countertop 1
                On the countertop 1, you see a butterknife 1, a cup 1, a fork 2, and a mug 1.
                > think: Now I find a mug (1). Next, I need to take it.
                Ok.
                > take mug 1 from countertop 1
                You pick up the mug 1 from the countertop 1.
                > think: Now I take a mug (1). Next, I need to heat it with stoveburner (1-4).
                Ok.
                > go to stoveburner 1
                On the stoveburner 1, you see a pan 2.
                > examine stoveburner 1
                On the stoveburner 1, you see a pan 2.
                > examine stoveburner 1
                On the stoveburner 1, you see a pan 2.
                > examine stoveburner 1
                On the stoveburner 1, you see a pan 2.
                > examine stoveburner 1
                On the stoveburner 1, you see a pan 2.
                STATUS: FAIL
                New plan: I was stuck in a loop in which I continually examined stoveburner 1 instead of heating mug 1 with stoveburner 1. I should have taken mug 1 from countertop 1, then heated it with stoveburner 1, then put it in coffeemachine 1. It did not help to execute two identical actions in a row. I will try to execute a different action if I am stuck in a loop again. 

                You are in the middle of a room. Looking quickly around you, you see a bed 1, a desk 2, a desk 1, a drawer 6, a drawer 5, a drawer 4, a drawer 3, a drawer 2, a drawer 1, a garbagecan 1, a laundryhamper 1, a safe 1, a shelf 6, a shelf 5, a shelf 4, a shelf 3, a shelf 2, and a shelf 1.
                Your task is to: look at bowl under the desklamp.
                > think: To solve the task, I need to find and take a bowl, then find and use a desklamp.
                OK.
                > think: First I need to find a bowl. A bowl is more likely to appear in drawer (1-6), desk (1-2), shelf (1-6), garbagecan (1), laundryhamper (1). I can check one by one, starting with drawer 1.
                OK.
                > go to drawer 1
                The drawer 1 is closed.
                > open drawer 1
                You open the drawer 1. The drawer 1 is open. In it, you see a cellphone 2.
                > go to drawer 2
                On the drawer 2, you see a keychain 1.
                > go to drawer 3
                Nothing happens.
                > go to drawer 4
                The drawer 4 is closed.
                > open drawer 4
                You open the drawer 4. The drawer 4 is open. In it, you see nothing.
                > go to drawer 5
                On the drawer 5, you see nothing.
                > go to drawer 6
                The drawer 6 is closed.
                > open drawer 6
                You open the drawer 6. The drawer 6 is open. In it, you see a book 2, and a pen 2.
                > go to desk 1
                On the desk 1, you see a alarmclock 1, a desklamp 1, a mug 1, and a pencil 1.
                > think: Now I find a desklamp (1). Next, I need to use it.
                OK.
                > use desklamp 1
                You turn on the desklamp 1.
                > 
                Nothing happens.
                > go to desk 2
                On the desk 2, you see a bowl 2, a bowl 1, a cd 2, a cd 1, and a creditcard 3.
                > think: Now I find a bowl (2). Next, I need to take it.
                OK.
                > take bowl 2 from desk 2
                You pick up the bowl 2 from the desk 2.
                > 
                Nothing happens.
                > 
                Nothing happens.
                STATUS: FAIL
                New plan: In this environment, my plan was to find a bowl then find and use a desklamp. However, the task says to look at bowl under the desklamp. I should have looked for the desklamp then looked for the bowl. I noticed that the desklamp was found on desk 1. In the next trial, I will go to desk 1, find the lamp, then look for the bowl under the desklamp.
                    """
            }]