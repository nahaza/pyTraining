# 2. Recursive Multiplication
# Design a recursive function that accepts two arguments into the parameters x and y. The
# function should return the value of x times y. Remember, multiplication can be performed
# as repeated addition as follows:
# 7 3 4 5 4 1 4 1 4 1 4 1 4 1 4 1 4
# (To keep the function simple, assume x and y will always hold positive nonzero integers.)

def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    result = mult(x, y)
    print(result)


def mult(x, y):
    if x != 0 or y != 0:
        return y + mult(x - 1, y)
    elif x == 0 or y == 0:
        return 0


if __name__ == '__main__':
    main()
