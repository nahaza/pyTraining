# 15. 1994 Weekly Gas Graph
# In the student sample programs for this book, you will find a text file named 1994_Weekly_
# Gas_Averages.txt. The file contains the average gas price for each week in the year 1994.
# (There are 52 lines in the file.) Using matplotlib, write a Python program that reads the
# contents of the file then plots the data as either a line graph or a bar chart. Be sure to display
# meaningful labels along the X and Y axes, as well as the tick marks.

import matplotlib.pyplot as plt


def getData(file):
    gasList = []
    gasDataFromFile = open(file, 'r')
    for x in gasDataFromFile:
        x = int(x.rstrip('\n'))
        gasList.append(x)
    return gasList


def getDateWeeks(gasList):
    dateWeekList = []
    for x in range(1, len(gasList) + 1):
        dateWeekList.append(x)
    return dateWeekList


def main():
    gasList = getData('gas.txt')
    dateList = getDateWeeks(gasList)

    xCoords = dateList
    yCoords = gasList

    plt.plot(xCoords, yCoords, marker='o')
    plt.title("The average gas price for each month of 1994")
    plt.xlabel('Month')
    plt.ylabel('Price, $')
    plt.xticks([3, 6, 9, 12],
               ['Mar', 'Jun', 'Sep', 'Dec'])
    plt.yticks([20, 30, 40, 50, 60],
               ['20', '30', '40', '50', '60'])
    plt.grid(True)
    plt.show()


main()
