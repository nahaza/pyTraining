# # Write a program that gives simple math quizzes.
# # The program should display two random numbers that are to be added,
# # such as: 247 + 129
# # The program should allow the student to enter the answer.
# # If the answer is correct, a message of congratulations should be displayed.
# # If the answer is incorrect,
# # a message showing the correct answer should be displayed.


import defFor11_12


def main():
    num1random = defFor11_12.getNum1Random()
    num2random = defFor11_12.getNum2Random()
    print("  ", num1random, "\n", "+", num2random)
    userAnswer = int(input("Enter the answer of operation: "))
    if userAnswer == defFor11_12.correctAnswer(num1random, num2random):
        print("Congratulations, it is the correct answer")
    else:
        print("Error. The correct answer is", defFor11_12.correctAnswer(num1random, num2random))


main()
