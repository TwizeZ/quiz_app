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
    
    # def score(self):
    #     return self.counter

class Quiz:
    def __init__(self, questions):
        self.score = 0
        self.questions = questions
    
    def play_quiz(self):
        print()
        print("===== WELCOME =====")

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

        for q in self.questions: # BUG: får det inte att fungera. Trodde man skulle använda range(rq). Fråga Nille.
            self.score += q.play_question()

        print("===== END =====")

        # qq = question_quantity()
        print(f"Your final score is {self.score} out of {rq}.")
        print("Thanks for playing!")
        print()

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
    Quiz().play_quiz()

# ---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    main()
    
    # print("As Ayrton Senna once said: 'If you no longer go for a gap that exits, you are no longer a racing driver.'")