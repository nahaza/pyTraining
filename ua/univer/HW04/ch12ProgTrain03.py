# 3. Recursive Lines
# Write a recursive function that accepts an integer argument, n. The function should display
# n lines of asterisks on the screen, with the first line showing 1 asterisk, the second line
# showing 2 asterisks, up to the nth line which shows n asterisks.


def main():
    n = int(input("Enter positive number: "))
    printAsterisks(n)


def printAsterisks(n):
    asteriks = '*'
    if n > 0:
        printAsterisks(n-1)
        print(asteriks * n)


if __name__ == '__main__':
    main()