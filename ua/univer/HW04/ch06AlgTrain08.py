# 8. A file exists on the disk named students.txt. The file contains several records, and
# each record contains two fields: (1) the student’s name, and (2) the student’s score for
# the final exam. Write code that changes Julie Milan’s score to 100.

import os


def main():
    found = False
    nameForGradeChange = 'Julie Milan'
    newGrade = 100
    studFile = open('stud.txt', 'r')
    tempFile = open('temp.txt', 'w')

    names = studFile.readline()
    while names != '':
        gradeInFile = int(studFile.readline())
        names = names.rstrip('\n')

        if names == nameForGradeChange:
            tempFile.write(names + '\n')
            tempFile.write(str(newGrade) + '\n')
            found = True
        else:
            tempFile.write(names + '\n')
            tempFile.write(str(gradeInFile) + '\n')

        names = studFile.readline()

    studFile.close()
    tempFile.close()

    os.remove('stud.txt')

    os.rename('temp.txt', 'stud.txt')

    if found:
        print('Updated')
    else:
        print('Not found')


main()
