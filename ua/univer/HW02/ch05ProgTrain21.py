# 20. Random Number Guessing Game
# Write a program that generates a random number in the range of 1 through 100, and asks
# the user to guess what the number is. If the user’s guess is higher than the random number,
# the program should display “Too high, try again.” If the user’s guess is lower than the
# 306 Chapter 5 Functions
# random number, the program should display “Too low, try again.” If the user guesses the
# number, the application should congratulate the user and generate a new random number
# so the game can start over.
# Optional Enhancement: Enhance the game so it keeps count of the number of guesses that
# the user makes. When the user correctly guesses the random number, the program should
# display the number of guesses.

import random

minNum = 1
maxNum = 100 + 1


def getRandomNumber(minNum, maxNum):
    number = random.randrange(minNum, maxNum)
    return number


def userAnswer():
    usAnswer = int(input("Enter the number: "))
    return usAnswer


def checkAnswer(num, usAnswer):
    if usAnswer > num:
        return "Too high"
    elif usAnswer < num:
        return "Too low"
    else:
        return "Congratulations. It is the correct answer"


def loopAfterIncorrect(guess, message, numRandom):
    while message != "Congratulations. It is the correct answer":
        print(message)
        print("Try again")
        answer = userAnswer()
        guess += 1
        message = checkAnswer(numRandom, answer)
        while message == "Congratulations. It is the correct answer":
            print(message)
            print("You won after", guess, "attempts")
            print("Guess the number")
            numRandom = getRandomNumber(minNum, maxNum)
            guess = 1
#            print(numRandom)
            answer = userAnswer()
            message = checkAnswer(numRandom, answer)


def loopAfterCorrect(guess, message):
    while message == "Congratulations. It is the correct answer":
        print(message)
        print("You won after", guess, "attempts")
        print("Guess the number")
        numRandom = getRandomNumber(minNum, maxNum)
        guess = 1
#        print(numRandom)
        answer = userAnswer()
        message = checkAnswer(numRandom, answer)
        while message != "Congratulations. It is the correct answer":
            print(message)
            print("Try again")
            answer = userAnswer()
            guess += 1
            message = checkAnswer(numRandom, answer)


def main():
    print("Guess the number")
    numRandom = getRandomNumber(minNum, maxNum)
#    print(numRandom)
    answer = userAnswer()
    guess = 1
    message = checkAnswer(numRandom, answer)
    if answer == numRandom:
        loopAfterCorrect(guess, message)
    elif answer != numRandom:
        loopAfterIncorrect(guess, message, numRandom)


main()
