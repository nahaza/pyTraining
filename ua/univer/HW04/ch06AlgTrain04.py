# 4. Write code that does the following: opens the number_list.txt file that was created
# by the code you wrote in question 3, reads all of the numbers from the file and displays
# them, then closes the file

def readNumbers():
    fromFile = open("number_list.txt", 'r')
    for x in fromFile:
        x = x.rstrip('\n')
        print(x)
    fromFile.close()


def main():
    readNumbers()


if __name__ == '__main__':
    main()
