# # TO STUDY LATER!!!!!!!!!
# 13. PowerBall Lottery
# To play the PowerBall lottery, you buy a ticket that has five numbers in the range of 1–69,
# and a “PowerBall” number in the range of 1–26. (You can pick the numbers yourself, or you
# can let the ticket machine randomly pick them for you.) Then, on a specified date, a winning
# set of numbers is randomly selected by a machine. If your first five numbers match the first
# five winning numbers in any order, and your PowerBall number matches the winning PowerBall number, then you win the jackpot, which is a very large amount of money. If your
# numbers match only some of the winning numbers, you win a lesser amount, depending on
# how many of the winning numbers you have matched.
# In the student sample programs for this book, you will find a file named pbnumbers.txt,
# containing the winning PowerBall numbers that were selected between February 3, 2010
# and May 11, 2016 (the file contains 654 sets of winning numbers). Figure 8-6 shows an
# example of the first few lines of the file’s contents. Each line in the file contains the set of six
# numbers that were selected on a given date. The numbers are separated by a space, and the
# last number in each line is the PowerBall number for that day. For example, the first line in
# the file shows the numbers for February 3, 2010, which were 17, 22, 36, 37, 52, and the
# PowerBall number 24.
# Write one or more programs that work with this file to perform the following:
# • Display the 10 most common numbers, ordered by frequency
# • Display the 10 least common numbers, ordered by frequency
# • Display the 10 most overdue numbers (numbers that haven’t been drawn in a long
# time), ordered from most overdue to least overdue
# • Display the frequency of each number 1–69, and the frequency of each Powerball
# number 1–26

def main():
    numberDict = {str(i): 0 for i in range(1, 70)}
    powerballDict = {str(i): 0 for i in range(1, 27)}
    f = open('pbnumbers.txt', 'r')
    for line in f:
        line = [int(i) for i in line.split(' ')]
        for i, num in enumerate(line):
            if i ==len(line)-1:
                powerballDict[str(num)] += 1
            else:
                numberDict[str(num)] += 1
    numberDict = numberDict.items()
    powerballDict = powerballDict.items()
    numberList = sorted(numberDict, key=lambda x:x[1], reverse=True)
    count = 0
    print("10 common numbers")
    while count < 10:
        print('{}:\t {}'.format(numberList[count][0],
                                numberList[count][1]))
        count += 1
    print()
    print()
    count = 0
    print("10 least numbers")
    while count < 10:
        if numberList[len(numberList) - count-1][1] != 0:
            print('{}:\t {}'.format(numberList[count][0],
                                    numberList[count][1]))
            count += 1
    print()
    print()
    count = 0
    print("frequency of each number (1-69")
    for num, val in numberDict:
        print('{}:\t {}'.format(num, val))
    print()
    print()
    print("frequency of each number (1-26")
    for num, val in powerballDict:
        print('{}:\t {}'.format(num, val))


if __name__ == '__main__':
    main()
