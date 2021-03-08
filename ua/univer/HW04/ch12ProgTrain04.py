# 4. Largest List Item
# Design a function that accepts a list as an argument and returns the largest value in the list.
# The function should use recursion to find the largest item.

def main():
    argList = [3, 5, 7, 2, 0, 9]
    print("The largest value in the list:", maxNumber(argList))


def maxNumber(x):
    if len(x) == 1:
        return x[0]
    else:
        if x[0] > maxNumber(x[1:]):
            return x[0]
        else:
            return maxNumber(x[1:])


main()
