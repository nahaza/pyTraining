# 21. Rock, Paper, Scissors Game
# Write a program that lets the user play the game of Rock, Paper, Scissors against the computer.
# The program should work as follows:
# 1. When the program begins, a random number in the range of 1 through 3 is generated.
# If the number is 1, then the computer has chosen rock. If the number is 2, then the
# computer has chosen paper. If the number is 3, then the computer has chosen scissors.
# (Don’t display the computer’s choice yet.)
# 2. The user enters his or her choice of “rock,” “paper,” or “scissors” at the keyboard.
# 3. The computer’s choice is displayed.
# 4. A winner is selected according to the following rules:
# •	 If one player chooses rock and the other player chooses scissors, then rock wins.
# (Rock smashes scissors.)
# •	 If one player chooses scissors and the other player chooses paper, then scissors wins.
# (Scissors cuts paper.)
# •	 If one player chooses paper and the other player chooses rock, then paper wins.
# (Paper wraps rock.)
# •	 If both players make the same choice, the game must be played again to determine
# the winner.

import random


def main():
    again()


def again():
    randomChoice = getRandomChoice()
    print(randomChoice)
    userChoice = getUserChoice()
    message, messageWinner = winner(randomChoice, userChoice)
    print("Robot's choice:", randomChoice)
    print("Your choice:", userChoice)
    print(message, messageWinner)
    again()


def getRandomChoice():
    choices = ['rock', 'paper', 'scissors']
    getRandomChoice = random.choice(choices)
    return getRandomChoice


def getUserChoice():
    userChoice = input("Make a choice: rock, paper or scissors: ")
    if userChoice == '' or userChoice == 'rock' or userChoice == 'paper' or userChoice == 'scissors':
        return userChoice
    print('Warning, enter rock, paper or scissors: ')
    return getUserChoice()


def winner(randomChoice, userChoice):
    rockMessage = 'Rock smashes scissors.'
    paperMessage = 'Paper wraps rock. '
    scissorsMessage = 'Scissors cuts paper.'
    messageNoWinner = 'It is a tie.'
    message = 'Let us try again.'
    messageWinner = 'No winners.'
    if randomChoice == userChoice:
        message = messageNoWinner
        messageWinner = 'No winners.'
        return message, messageWinner
    else:
        if randomChoice == 'rock':
            if userChoice == 'scissors':
                message = rockMessage
                messageWinner = 'You lose. '
            elif userChoice == 'paper':
                message = paperMessage
                messageWinner = 'You won. '
        elif randomChoice == 'paper':
            if userChoice == 'scissors':
                message = scissorsMessage
                messageWinner = 'You won. '
            elif userChoice == 'rock':
                message = paperMessage
                messageWinner = 'You lose. '
        elif randomChoice == 'scissors':
            if userChoice == 'rock':
                message = rockMessage
                messageWinner = 'You won. '
            elif userChoice == 'paper':
                message = scissorsMessage
                messageWinner = 'You lose. '
        return message, messageWinner


main()
