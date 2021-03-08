# 9. Exception Handing
# Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
# •	 It should handle any IOError exceptions that are raised when the file is opened and data
# is read from it.
# •	 It should handle any ValueError exceptions that are raised when the items that are read
# from the file are converted to a number.


def main():
    try:
        total = 0
        numCount = 0
        fromFile = open('numbers.txt', 'r')
        numb = fromFile.readline()
        while numb != '':
            numb = int(numb.rstrip('\n'))
            total += numb
            numCount += 1
            numb = fromFile.readline()
        numAver = total / numCount
    except IOError as err:
        print("It is IOError", err)
    except ValueError as err:
        print("It is ValueError", err)
    else:
        print("Average is: ", format(numAver, '.2f'))


if __name__ == '__main__':
    main()
