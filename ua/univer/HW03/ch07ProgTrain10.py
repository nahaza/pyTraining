# 10. World Series Champions
# If you have downloaded the source code you will find a file named WorldSeriesWinners.
# txt in the Chapter 07 folder. This file contains a chronological list of the World Series winning teams from 1903 through 2009. (The first line in the file is the name of the team that
# won in 1903, and the last line is the name of the team that won in 2009. Note the World
# Series was not played in 1904 or 1994.)
# Write a program that lets the user enter the name of a team, then displays the number of
# times that team has won the World Series in the time period from 1903 through 2009.

def readFile(file):
    championsFile = open(file, 'r')
    championsList = []
    champions = championsFile.readline()
    while champions != '':
        champions = champions.rstrip('\n')
        championsList.append(champions)
        champions = championsFile.readline()
    return championsList


def getVictoryTimes(championNameUser, listChampions):
    victoryTimes = 0
    for chapIndex in range(len(listChampions)):
        if listChampions[chapIndex] == championNameUser:
            victoryTimes += 1
    return victoryTimes


def printResult(nameChamp, victoryTimes):
    print(nameChamp, "won", victoryTimes, "times")


def main():
    file = "champions.txt"
    championsList = readFile("champions.txt")
    championNameUser = input("Enter the team to check: ")
    victoryTimes = getVictoryTimes(championNameUser, championsList)
    printResult(championNameUser, victoryTimes)


main()
