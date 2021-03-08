# 10. Golf Scores
# The Springfork Amateur Golf Club has a tournament every weekend. The club president
# has asked you to write two programs:
# 1. A program that will read each player’s name and golf score as keyboard input, then
# save these as records in a file named golf.txt. (Each record will have a field for the
# player’s name and a field for the player’s score.)
# 2. A program that reads the records from the golf.txt file and displays them.

def contentPlayers():
    name = input("Enter player's name: ")
    return name


def contentScores(name):
    score = int(input("Enter score of " + name + ": "))
    return score


def writeToFile():
    again = "y"
    toFromFile = open("golf.txt", 'w')
    while again == "y" or again == "Y":
        name = contentPlayers()
        score = contentScores(name)
        toFromFile.write(name + '\n' + str(score) + '\n')
        again = input("Keep input? Enter y as yes: ")
    toFromFile.close()
    print("Updated")


def readName():
    toFromFile = open("golf.txt", 'r')
    name = toFromFile.readline().rstrip('\n')
    while name != '':
        score = str(toFromFile.readline()).rstrip('\n')
        print(name + " " + score)
        name = toFromFile.readline().rstrip('\n')
    toFromFile.close()


def main():
    writeToFile()
    readName()


if __name__ == '__main__':
    main()
