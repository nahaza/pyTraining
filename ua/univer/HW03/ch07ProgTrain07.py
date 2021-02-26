# 7. Driver’s License Exam
# The local driver’s license office has asked you to create an application that grades the
# written portion of the driver’s license exam. The exam has 20 multiple-choice questions. Here
# are the correct answers:
# 1. A
# 2. C
# 3. A
# 4. A
# 5. D
# 6. B
# 7. C
# 8. A
# 9. C
# 10. B
# 11. A
# 12. D
# 13. C
# 14. A
# 15. D
# 16. C
# 17. B
# 18. B
# 19. D
# 20. A
# Your program should store these correct answers in a list. The program should read the
# student’s answers for each of the 20 questions from a text file and store the answers in
# another list. (Create your own text file to test the application.) After the student’s answers
# have been read from the file, the program should display a message indicating whether the
# student passed or failed the exam. (A student must correctly answer 15 of the 20 questions
# to pass the exam.) It should then display the total number of correctly answered questions,
# the total number of incorrectly answered questions, and a list showing the question numbers of
# the incorrectly answered questions.


def answerCorrect():
    listCorrect = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                   'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    return listCorrect


def answerUser():
    listUser = []
    openFile = open('answuser.txt', 'r')
    for x in openFile:
        x = x.rstrip('\n')
        listUser.append(x)
    return listUser


def check(listCorrect, listUser):
    count = 0
    answerWrong = []
    for x in range(20):
        if listUser[x] == listCorrect[x]:
            count +=1
        else:
            answerWrong.append(x)
    if count <15:
        print("You did not pass the exam")
    else:
        print("You passed the exam")

    print("The total number of correctly answered questions", count)
    print("The total number of incorrectly answered questions",20 -count)
    print("Question numbers of the incorrectly answered questions:", answerWrong)


def main():
    listCorrect = answerCorrect()
    listUser = answerUser()
    check(listCorrect, listUser)

main()
