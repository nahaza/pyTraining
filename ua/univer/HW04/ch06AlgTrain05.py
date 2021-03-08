# 5. Modify the code that you wrote in problem 4 so it adds all of the numbers read from
# the file and displays their total.

def readNumbers():
    total = 0
    fromFile = open("number_list.txt", 'r')
    for x in fromFile:
        x = int(x.rstrip('\n'))
        total += x
    print(total)
    fromFile.close()


def main():
    readNumbers()


if __name__ == '__main__':
    main()
