# 1. File Display
# Assume a file containing a series of integers is named numbers.txt
# and exists on the computer’s disk. Write a program that displays all of the numbers in the file.

def main():
    numInFile = open('number_list.txt', 'r')
    for numbers in numInFile:
        numbers = int(numbers.rstrip('\n'))
        print(numbers)
    numInFile.close()


if __name__ == '__main__':
    main()
