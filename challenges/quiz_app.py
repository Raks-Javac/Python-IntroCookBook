# ##### Challenge 9

#  9.⁠ ⁠Quiz Program:
# Create a program that asks users a series of questions, keeps track of their scores, and then reports their final score.



class Questions:
    def __init__(self,question = "", answer = False):
        self.question = question
        self.answer = answer

    @staticmethod
    def dummy_q() -> list:
         return  [
    Questions(
        question="The sky is blue?",
        answer=True
    ),
    Questions(
        question="The sun rises in the west?",
        answer=False
    ),
    Questions(
        question="There are seven days in a week?",
        answer=True
    ),
    Questions(
        question="Water freezes at 0 degrees Celsius?",
        answer=True
    ),
    Questions(
        question="Cats can fly?",
        answer=False
    ),
    Questions(
        question="The capital of France is Berlin?",
        answer=False
    ),
    Questions(
        question="An octopus has three hearts?",
        answer=True
    ),
    Questions(
        question="The Great Wall of China is visible from space?",
        answer=False
    ),
    Questions(
        question="Light travels faster than sound?",
        answer=True
    ),
    Questions(
        question="Humans have walked on Mars?",
        answer=False
    ),
]

class QuizApp:
    def __init__(self):
        self.questions = Questions.dummy_q() 
        self.score = 0

    def welcome_user(self):
        print("The question bot only takes in 'y' as Yes and 'n' as No")
    def take_user_input(self):
        try:
             user_answer = str(input("Answer: ")).lower()
             if(user_answer != "N" or user_answer != "Y"):
                 if(user_answer == "y"):
                     return True
                 else:
                     return False
             else:
                 return False
        except:
            print("Error taking input")
            self.take_user_input()
            return False

    def start_quiz(self):
        for q in self.questions:
            print(q.question)
            if (self.take_user_input()) == q.answer:
                self.score += 1
        print(f"Your quiz score is {self.score}")



# Start quiz app
quiz_app = QuizApp()
