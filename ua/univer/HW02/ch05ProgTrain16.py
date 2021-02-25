# 16. Test Average and Grade
# Write a program that asks the user to enter five test scores. The program should display a
# letter grade for each score and the average test score. Write the following functions in the
# program:
# •	 calc_average. This function should accept five test scores as arguments and return the
# average of the scores.
# •	 determine_grade. This function should accept a test score as an argument and return
# a letter grade for the score based on the following grading scale:
# Score Letter Grade
# 90–100 A
# 80–89 B
# 70–79 C
# 60–69 D
# Below 60 F

num = 5

def main():
    total = 0
    for x in range(1, num+1):
        score = int(input("Enter the test score"+str(x)+": "))
        letter = determineGrade(score)
        print("Letter grade for the score:", letter)
        total += score
    average = calcAverage(total)
    print("The average of the scores:", format(average, '.0f'))



def calcAverage(total):
    aver = total / num
    return aver


def determineGrade(score):
    if score >= 90:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    elif score < 60:
        return "F"


main()
