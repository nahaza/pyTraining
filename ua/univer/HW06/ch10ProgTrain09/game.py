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

class Question:
    player_1 = 0
    player_2 = 0

    def __init__(self, question, answer, c_answer):
        self.question = question
        self.answer = answer
        self.c_answer = c_answer

    def test1(self):
        if self.c_answer.lower() == self.answer:
            print("Correct")
            print()
            Question.player_1 += 1
        else:
            print("Wrong. Correct answer:", self.answer)
            print()

    def get_test1(self):
        return Question.player_1

    def test2(self):
        if self.c_answer.lower() == self.answer:
            print("Correct")
            print()
            Question.player_2 += 1
        else:
            print("Wrong. Correct answer:", self.answer)
            print()

    def get_test2(self):
        return Question.player_2

    def __str__(self):
        return "Player 1: " + str(Question.player_1) + "Player 2: " + str(Question.player_2)
