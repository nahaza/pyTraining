# 8. Name Search
# If you have downloaded the source code you will find the following files in the Chapter 07
# folder:
# •	 GirlNames.txt This file contains a list of the 200 most popular names given to girls
# born in the United States from the year 2000 through 2009.
# •	 BoyNames.txt This file contains a list of the 200 most popular names given to boys
# born in the United States from the year 2000 through 2009.
# Write a program that reads the contents of the two files into two separate lists. The user
# should be able to enter a boy’s name, a girl’s name, or both, and the application will display
# messages indicating whether the names were among the most popular.

def namesList(file):
    listName = []
    name = open(file, 'r')
    for x in name:
        listName.append(x.rstrip('\n'))
    return listName


def main():
    nameGirl = namesList('girls.txt')
    nameBoy = namesList('boys.txt')
    nameUser = input("Enter the name to search: ")
    find = 0
    if nameUser in nameGirl:
        find = 1
        print(nameUser, "is in the list of popular girl's names")
    if nameUser in nameBoy:
        find = 1
        print(nameUser, "is in the list of popular boy's names")
    if find == 0:
        print("It is unpopular name")


main()
