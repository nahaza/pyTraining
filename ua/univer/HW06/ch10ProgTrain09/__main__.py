# 9. Trivia Game
# In this programming exercise, you will create a simple trivia game for two players. The program will work like this:
# • Starting with player 1, each player gets a turn at answering 5 trivia questions. (There
# should be a total of 10 questions.) When a question is displayed, 4 possible answers are
# also displayed. Only one of the answers is correct, and if the player selects the correct
# answer, he or she earns a point.
# • After answers have been selected for all the questions, the program displays the number
# of points earned by each player and declares the player with the highest number of points
# the winner.572 Chapter 10 Classes and Object-Oriented Programming
# To create this program, write a Question class to hold the data for a trivia question. The
# Question class should have attributes for the following data:
# • A trivia question
# • Possible answer 1
# • Possible answer 2
# • Possible answer 3
# • Possible answer 4
# • The number of the correct answer (1, 2, 3, or 4)
# The Question class also should have an appropriate _ _init_ _ method, accessors, and
# mutators.
# The program should have a list or a dictionary containing 10 Question objects, one for
# each trivia question. Make up your own trivia questions on the subject or subjects of your
# choice for the objects.

import game


def main():
    question_objects = []
    questions = [
        "What is the capital of Turkey?\n \
        (a) Istanbul\n(b) Ankara\n(c) Izmir\n (d) Antalya",
        "What is the capital of France?\n \
        (a) London\n(b) Paris\n(c) Kyiv\n (d) Washington"]

    answers = ["b", "b"]
    print("Player 1 questions: ")
    print()
    for i in range(0, int(len(questions)/2), 1):
        print("Question: ", i+1)
        print(questions[i])
        user_answer = input("Enter correct answer (a , b, c, d): ")
        question = game.Question(questions[i], answers[i], user_answer)
        question_objects.append(question)
        question.test1()
    question_objects = []
    print("_________________________________________________")
    print("Player 2 questions: ")
    print()
    for i in range(int(len(questions) / 2), len(questions), 1):
        print("Question: ", i + 1)
        print(questions[i])
        user_answer = input("Enter correct answer (a , b, c, d): ")
        question = game.Question(questions[i], answers[i], user_answer)
        question_objects.append(question)
        question.test2()
    if question.get_test1() > question.get_test2():
        print("Player 1 won")
    elif question.get_test2() > question.get_test1():
        print("Player 2 won")
    else:
        print("It is a draw")
    print()
    print("Player 1 score: ", question.get_test1())
    print("Player 2 score: ", question.get_test2())


main()
