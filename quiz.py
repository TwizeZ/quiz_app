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
# WHILE-sats här? while round <= round_quantity
        print("===== QUESTION =====")
        print(self.question)
        print()
        print("===== ALTERNATIVES =====")
        for alt in self.choices:
            print(alt)
        print()
        answer = input("Your answer: ")
        if answer == self.answer:
            print("Congratulations! Senna would have been proud...")
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

def main(rq):
    round = 1
    
    question = load_question()
    random.shuffle(question)
    for round in range(rq):
        question[round].play_question() #kan inte köra fler rundor än frågor


    # for q in question:
    #     q.play_question()



if __name__ == "__main__":
    print("Welcome!")

# number of rounds you would like to play

    while True:
        round_quantity = int(input("How many rounds would you like to play? Max number of rounds is 10.\n"))

        if round_quantity > 10 or round_quantity < 1:
            print("Not a valid answer! Please choose between 1-10 rounds:")
        else:
            break

    start = input(f"{round_quantity} number of rounds selected. Press Enter to continue: ")
    print()
    print()
    
    if "" in start:
        pass

#    for i in range(round_quantity):
    main(round_quantity)
    
    print("===== END =====")
    print("Thanks for playing!")