# 7. Recursive Power Method
# Design a function that uses recursion to raise a number to a power. The function should
# accept two arguments: the number to be raised, and the exponent. Assume the exponent is
# a nonnegative integer.

def main():
    num = int(input("Enter a number: "))
    power = int(input("Enter a power: "))
    print(mult(num, power))


def mult(x, y):
    if y == 1:
        return x
    elif y == 0:
        return 0
    else:
        return x * mult(x, y-1)


main()
