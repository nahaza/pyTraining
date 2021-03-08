# 6. Average of Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the
# computer’s disk. Write a program that calculates the average of all the numbers stored in
# the file.

def main():
    total = 0
    numCount = 0
    fromFile = open('numbers.txt', 'r')
    numb = fromFile.readline()
    while numb != '':
        numb = int(numb.rstrip('\n'))
        total += numb
        numCount += 1
        numb = fromFile.readline()
    numAver = total / numCount
    print("Average is: ", format(numAver, '.2f'))
    fromFile.close()


if __name__ == '__main__':
    main()
