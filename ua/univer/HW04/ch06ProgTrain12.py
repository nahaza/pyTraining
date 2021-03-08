# 12. Average Steps Taken
# A Personal Fitness Tracker is a wearable device that tracks your physical activity, calories
# burned, heart rate, sleeping patterns, and so on. One common physical activity that most
# of these devices track is the number of steps you take each day.
# If you have downloaded this book’s source code from the Premium Companion Website,
# you will find a file named steps.txt in the Chapter 06 folder. (The Premium Companion
# Website can be found at www.pearsonglobaleditions.com/gaddis.) The steps.txt file
# contains the number of steps a person has taken each day for a year. There are 365 lines
# in the file, and each line contains the number of steps taken during a day. (The first line is
# the number of steps taken on January 1st, the second line is the number of steps taken on
# January 2nd, and so forth.) Write a program that reads the file, then displays the average
# number of steps taken for each month. (The data is from a year that was not a leap year,
# so February has 28 days.)

# import random
#
#
# def getNumRand():
#     numRand = random.randint(1, 70000)
#     return numRand
#
#
# def main():
#     lineNum = int(input("Enter the number of random numbers: "))
#     toFile = open("numbers12.txt", 'a')
#     num = 0
#     for x in range(1, lineNum + 1):
#         numRan = getNumRand()
#         toFile.write(str(numRan) + '\n')
#     toFile.close()
#     print("Updated")
#
#
# if __name__ == '__main__':
#     main()


def main():
    daysMonth = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    month = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December')
    total = 0
    fromFile = open('numbers12.txt', 'r')
    monthNum = 0
    for x in range(1, 13):
        stepsTotal = 0
        aver = 0
        for y in range(1, daysMonth[monthNum] + 1):
            steps = int(fromFile.readline().rstrip('\n'))
            stepsTotal += steps
        aver = stepsTotal / daysMonth[monthNum]
        print("Average steps for month " + month[monthNum] + ": " + format(aver, '.0f') + " steps")
        monthNum += 1


if __name__ == '__main__':
    main()
