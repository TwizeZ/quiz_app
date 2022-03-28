#Felix Larsson
#TEINF-20
#Quiz application
#16-03-2022

import random

class Question:
    def __init__(self, question : str, answer : str, choices : list()):
        self.question = question
        self.answer = answer
        self.choices = choices
        random.shuffle(self.choices)

    def get_name(self):
        return self.question

    def get_answer(self):
        return self.answer

    def get_choices(self):
        return self.choices
    
    def play_question(self):
        self.score = 0
        print("===== QUESTION =====")
        print(self.question)
        print()
        print("===== ALTERNATIVES =====")
        for alt in self.choices:
            print(alt)
        print()
        answer = input("Your answer: ")
        if answer.casefold() == self.answer.casefold():
            self.score += 1
            print(f"Well done! {self.answer} is correct.")
            print()
            print()
            print()
        else:
            print(f"That was a tough one, huh? The right answer was {self.answer}.")
            print()
            print()
            print()
        return self.score
    
    # def score(self):
    #     return self.counter

class Quiz:
    def play_quiz():
        round = 1    

        while True:
            qq = question_quantity()
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

        question = load_question()
        random.shuffle(question)
        for round in range(rq):
            question[round].play_question()

# ---------------------------------------------------------------------------------------------------------

def load_question():
    questions = []
    with open("questions.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            selection = line.split("/")
            quiz = Question(selection[0],
                            selection[1],
                            selection[2].split(","))
            
            questions.append(quiz)
    return questions

def question_quantity():
    with open("questions.txt", "r", encoding="utf8") as fp:
        qtot = len(fp.readlines())
    return qtot    

# ---------------------------------------------------------------------------------------------------------

def main():
    Quiz.play_quiz()

# ---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    print()
    print("===== WELCOME =====")
    
    main()
    
    print("===== END =====")

    # qq = question_quantity()
    print(f"Your final score is [PLACEHOLDER] out of [PLACEHOLDER].") # BUG: Score får fel output. Fråga Niclas på tisdag.
    print("Thanks for playing!")
    print()
    print("As Ayrton Senna once said: 'If you no longer go for a gap that exits, you are no longer a racing driver.'")