# 9. Population Data
# If you have downloaded the source code you will find a file named USPopulation.txt
# in the Chapter 07 folder. The file contains the midyear population of the United States, in
# thousands, during the years 1950 through 1990. The first line in the file contains the population for 1950, the second line contains the population for 1951, and so forth.
# Write a program that reads the file’s contents into a list. The program should display the
# following data:
# •	 The average annual change in population during the time period
# •	 The year with the greatest increase in population during the time period
# •	 The year with the smallest increase in population during the time period

def dataFromFile(file):
    populationlist = []
    populationFromFile = open(file, 'r')
    populationYear = populationFromFile.readline()

    while populationYear != '':
        populationYear = int(populationYear)
        populationlist.append(populationYear)
        populationYear = populationFromFile.readline()
    return populationlist


def populationChange(populationlist):
    changeList = []
    for yearIndex in range(len(populationlist)):
        if yearIndex == 0:
            changeList.append(0)
        else:
            changeList.append(populationlist[yearIndex] - populationlist[yearIndex - 1])
    return changeList


def averageChange(changeList):
    totalChange = 0
    for changeIndex in range(len(changeList)):
        totalChange = totalChange + changeList[changeIndex]

    averageChangePop = totalChange / len(changeList)
    return averageChangePop


def getMaxChange(changeList, firstYear):
    maxChange = max(changeList)
    maxChangeIndex = changeList.index(maxChange)
    maxChangeYear = maxChangeIndex + firstYear
    return maxChangeYear, maxChange


def getMinChange(changeList, firstYear):
    minChange = max(changeList)
    minChangeIndex = changeList.index(minChange)
    minChangeYear = minChangeIndex + firstYear
    return minChangeYear, minChange


def printData(averageChangePop, maxChangeYear, maxChange, minChangeYear, minChange):
    print("The average annual change in population during the time period: ", averageChangePop)
    print("The year with the greatest increase in population during the time period:", maxChangeYear, "by", maxChange)
    print("The year with the smallest increase in population during the time period", minChangeYear, "by", minChange)


def main():
    file = 'population.txt'
    firstYear = 1950
    populationlist = dataFromFile('population.txt')
    changeList = populationChange(populationlist)
    averageChangePop = averageChange(changeList)
    maxChangeYear, maxChange = getMaxChange(changeList, firstYear)
    minChangeYear, minChange = getMinChange(changeList, firstYear)
    printData(averageChangePop, maxChangeYear, maxChange, minChangeYear, minChange)


main()
