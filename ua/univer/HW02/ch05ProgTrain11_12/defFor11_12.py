import random


def getNum1Random():
    return random.randint(1, 100)


def getNum2Random():
    return random.randint(1, 100)


def correctAnswer(num1random, num2random):
    return num1random + num2random
