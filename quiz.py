#Felix Larsson
#TEINF-20
#Quiz application
#16-03-2022

class Question:
    def __init__(self, question : str, answer : str, choices : str):
        self.question = question
        self.answer = answer
        self.choices = choices

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



def main():
    round = 1
    questions = load_question()

    

if __name__ == "__main__":
    print("Welcome!")
    start = input("Press any key to continue: ")
    if "" in start:
        pass
    main()