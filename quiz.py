#Felix Larsson
#TEINF-20
#Quiz application
#16-03-2022

import random
from time import sleep

class Question:
    def __init__(self, question : str, answer : str, choices : list()):
        self.question = question
        self.answer = answer
        self.choices = choices
        random.shuffle(self.choices)
    
    def play_question(self):
        print("===== QUESTION =====")
        print(self.question)
        print()
        print("===== ALTERNATIVES =====")
        for alt in self.choices:
            print(alt)
        print()
        answer = input("Your answer: ")
        if answer.casefold() == self.answer.casefold():
            print(f"Well done! {self.answer} is correct.")
            print()
            print()
            return 1
        else:
            print(f"That was a tough one, huh? The right answer was {self.answer}.")
            print()
            print()
            return 0

class Quiz:
    def __init__(self):
        self.score = 0

    def play_quiz(self):
        print()
        print("===== WELCOME =====")

        while True:
            choice = int(input(f"What topic do you want the quiz to be about? You can choose between:\n1. Cars\n2. NTI\n3. Music\n"))
            if choice > 3 or choice < 1:
                print("Not a valid answer! Please choose between the options displayed.")
                continue
            else:
                break

        while True:
            qq = question_quantity(int(choice))
            rq = int(input(f"How many rounds would you like to play? Max number of rounds is {qq}.\n"))
            if rq > qq or rq < 1:
                print(f"Not a valid answer! Please choose between 1-{qq} rounds:")
                continue
            else:
                break

        start = input(f"{rq} number of rounds selected.\nPress Enter to continue: ")
        print()
        print()
        if "" in start:
            pass

        self.questions = load_question(int(choice))
        random.shuffle(self.questions)
        for round in range(rq):
            self.score += self.questions[round].play_question()

        print("===== END =====")

        print(f"Your final score is {self.score} out of {rq}.")
        print("Thanks for playing!")
        print()

# ---------------------------------------------------------------------------------------------------------

def load_question(choice : int):
    path = ""
    if choice == 1:
        path='cars.txt'
    elif choice == 2:
        path='nti.txt'
    elif choice == 3:
        path='music.txt' 
    
    questions = []
    with open(path, "r", encoding="utf8") as f:
        for line in f.readlines():
            selection = line.split("/")
            quiz = Question(selection[0],
                            selection[1],
                            selection[2].split(","))
            
            questions.append(quiz)
    return questions

def question_quantity(choice : int):
    path = ""
    if choice == 1:
        path='cars.txt'
    elif choice == 2:
        path='nti.txt'
    elif choice == 3:
        path='music.txt' 
    
    with open(path, "r", encoding="utf8") as fp:
        qtot = len(fp.readlines())
    return qtot    

# ---------------------------------------------------------------------------------------------------------

def main():
    Quiz().play_quiz()

# ---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    main()

    while True:
        replay = input("Would you like to play again?\n")
        if replay.casefold() == "yes".casefold() or replay.casefold() == "yezzzelitoo".casefold(): # Adams lilla easter egg
            print("Very well! Restarting quiz...")
            sleep(2)
            print()
            print()
            print()
            main()
        else:
            print("That's fine. Have a good day!")
            print()
            break