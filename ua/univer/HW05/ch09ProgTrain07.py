# 7. World Series Winners
# In this chapter’s source code folder (available on the Premium Companion Website at www.
# pearsonglobaleditions.com/gaddis), you will find a text file named WorldSeriesWinners.
# txt. This file contains a chronological list of the World Series’ winning teams from 1903
# through 2009. The first line in the file is the name of the team that won in 1903, and the
# last line is the name of the team that won in 2009. (Note the World Series was not played
# in 1904  or 1994. There are entries in the file indicating this.)
# Write a program that reads this file and creates a dictionary in which the keys are the names
# of the teams, and each key’s associated value is the number of times the team has won the
# World Series. The program should also create a dictionary in which the keys are the years,
# and each key’s associated value is the name of the team that won that year.
# The program should prompt the user for a year in the range of 1903 through 2009. It
# should then display the name of the team that won the World Series that year, and the
# number of times that team has won the World Series.

def main():
    fromFile = open('champions.txt', 'r')
    dataFromFile = fromFile.read().splitlines()
    fromFile.close()
    dictNames = {}
    dictYears = {}
    again = 'y'
    for name in dataFromFile:
        if name in dictNames:
            dictNames[name] += 1
        else:
            dictNames[name] = 1
    year = 1903
    for name in dataFromFile:
        dictYears[year] = name
        year += 1
    print(dictYears)
    print(dictNames)
    again = 'y'
    while again == 'y':
        year = int(input("Enter the year: "))
        if year != 1904 and year != 1913 and 1903 <= year <= 1914:
            print("The team that won the World Series that year: ", dictYears[year])
            print("This team won the cup", dictNames[dictYears[year]], "times")
        else:
            print("Enter the correct year")
        again = input("Do you want to play again? Enter y for yeas: ")


if __name__ == '__main__':
    main()
