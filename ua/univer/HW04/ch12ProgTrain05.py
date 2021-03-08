# 5. Recursive List Sum
# Design a function that accepts a list of numbers as an argument.
# The function should recursively calculate the sum of all the numbers in the list and return that value.

def main():
    numList = [3, 5, 4, 2, 1, 0]
    print(numSum(numList))


def numSum(x):
    if len(x) == 1:
        return x[0]
    else:
        return x[0]+numSum(x[1:])


main()
