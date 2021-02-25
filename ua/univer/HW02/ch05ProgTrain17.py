# 17. Odd/Even Counter
# In this chapter, you saw an example of how to write an algorithm that determines
# whether a number is even or odd. Write a program that generates 100 random numbers
# and keeps a count of how many of those random numbers are even, and how many of
# them are odd.

import random

howMany = 100


def main():
    numberOfEven = 0
    numberOfOdd = 0
    for x in range(1, howMany+1):
        num = random.randrange(1, howMany)
        if even(num):
            numberOfEven += 1
        else:
            numberOfOdd += 1
        print(num)
    print("Number of even numbers:", numberOfEven)
    print("Number of odd numbers:", numberOfOdd)


def even(num):
    if (num % 2) == 0:
        return True
    return False


main()