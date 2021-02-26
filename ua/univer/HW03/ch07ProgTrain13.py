# 13. Magic 8 Ball
# Write a program that simulates a Magic 8 Ball, which is a fortune-telling toy that displays a
# random response to a yes or no question. In the student sample programs for this book, you
# will find a text file named 8_ball_responses.txt. The file contains 12 responses, such
# as “I don’t think so”, “Yes, of course!”, “I’m not sure”, and so forth. The program should
# read the responses from the file into a list. It should prompt the user to ask a question, then
# display one of the responses, randomly selected from the list. The program should repeat
# until the user is ready to quit.
# 428 Chapter 7 Lists and Tuples
# Contents of 8_ball_responses.txt:
# Yes, of course!
# Without a doubt, yes.
# You can count on it.
# For sure!
# Ask me later.
# I’m not sure.
# I can’t tell you right now.
# I’ll tell you after my nap.
# No way!
# I don’t think so.
# Without a doubt, no.
# The answer is clearly NO.

import random


def getAnswerList(file):
    answerList = []
    answerData = open(file, 'r')
    for x in answerData:
        x = x.rstrip('\n')
        answerList.append(x)
    return answerList


def getRandAnswer(answerList):
    answer = random.choice(answerList)
    return answer


def playAgain():
    again = 'y'
    while again == 'y':
        again = input("Keep going? Enter y as yes: ")
    return again


def main():
    answerList = getAnswerList('magicball.txt')
    again = 'y'
    while again == 'y':
        questionUser = input("Enter your question: ")
        answer = getRandAnswer(answerList)
        print(answer)
        again = input("Keep going? Enter y as yes: ")


main()
