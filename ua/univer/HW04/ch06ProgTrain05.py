# 5. Sum of Numbers
# Assume a file containing a series of integers is named numbers.txt and exists
# on the computer’s disk. Write a program that reads all of the numbers stored in the file and calculates
# their total.

def main():
    total = 0
    fromFile = open('numbers.txt', 'r')
    numb = fromFile.readline()
    for numb in fromFile:
        numb = int(numb.rstrip('\n'))
        total += numb
        numb = fromFile.readline()
    print(total)
    fromFile.close()


if __name__ == '__main__':
    main()

