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
        self.counter = 0

    def get_name(self):
        return self.question

    def get_answer(self):
        return self.answer

    def get_choices(self):
        return self.choices
    
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
            self.counter += 1
            print("Well done! Keep this up.")
            print()
            print()
            print()
        else:
            print(f"That was a tough one, huh? The right answer was {self.answer}.")
            print()
            print()
            print()
    
    def score(self):
        return self.counter

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
    round = 1    

# number of rounds you would like to play in a loop

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

# question generator

    question = load_question()
    random.shuffle(question)
    for round in range(rq):
        question[round].play_question()

    # for q in question:
    #     q.play_question()

# ---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    print("Welcome!")
    main()
    
# end quote
    print("===== END =====")

    qq = question_quantity()
    score = Question.score
    print(f"Your final score is {score} out of {qq}.") # BUG: Score får fel output. Fråga Niclas på tisdag.
    print("Thanks for playing!")
    print()
    print("As Ayrton Senna once said: 'If you no longer go for a gap that exits, you are no longer a racing driver.'")