def pritn_10_positive():
    i = 0
    while i < 10:
        value = int(input("Enter positive value: "))
        if value >= 0:
            i += 1
            print("count=", i, "value =", value)
        else:
            print("Not positive")


def power(x, n):
    value = 1
    for i in range(n):
        value *= x
    return value


def calc_power_from_console():
    x = int(input("Enter value x: "))
    n = int(input("Enter power n: "))
    print("x =", x, "in power", n, "=", power(x, n))