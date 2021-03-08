# 7. A file exists on the disk named students.txt. The file contains several records, and
# each record contains two fields: (1) the student’s name, and (2) the student’s score
# for the final exam. Write code that deletes the record containing “John Perz” as the
# student name.

# def main():
#    num_stud = int(input('How many students: '))
#    emp_file = open('stud.txt', 'w')
#    for count in range(1, num_stud + 1):
#        name = input('Name: ')
#        grade = int(input('Grade: '))
#        emp_file.write(name + '\n')
#        emp_file.write(str(grade) + '\n')
#    emp_file.close()
#
#
# main()

import os


def main():
    found = False
    nameToRemove = 'John Perz'
    removeFromFile = open('stud.txt', 'r')
    tempFile = open('temp.txt', 'w')

    names = removeFromFile.readline()
    while names != '':
        gradeInFile = int(removeFromFile.readline())
        names = names.rstrip('\n')

        if names != nameToRemove:
            tempFile.write(names + '\n')
            tempFile.write(str(gradeInFile) + '\n')
        else:
            found = True

        names = removeFromFile.readline()

    removeFromFile.close()
    tempFile.close()

    os.remove('stud.txt')

    os.rename('temp.txt', 'stud.txt')

    if found:
        print('Updated')
    else:
        print('Not found')


main()
