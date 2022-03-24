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
        if answer == self.answer:
            print("Well done! Keep this up.")
            print()
            print()
            print()
        else:
            print(f"That was a tough one, huh? The right answer was {self.answer}.")
            print()
            print()
            print()



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

# ---------------------------------------------------------------------------------------------------------

def main():
    round = 1

# number of rounds you would like to play in a loop

    while True:
        rq = int(input("How many rounds would you like to play? Max number of rounds is 10.\n"))

        if rq > 10 or rq < 1:
            print("Not a valid answer! Please choose between 1-10 rounds:")
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
        question[round].play_question() #kan inte köra fler rundor än frågor

    # for q in question:
    #     q.play_question()

# ---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    print("Welcome!")
    main()
    
# end quote
    print("===== END =====")
    print("As Ayrton Senna once said: 'If you no longer go for a gap that exits, you are no longer a racing driver.'")
    print("Thanks for playing!")