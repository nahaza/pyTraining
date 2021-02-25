# 7. Stadium Seating
# There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost
# $15, and Class C seats cost $10. Write a program that asks how many tickets for each class
# of seats were sold, then displays the amount of income generated from ticket sales.

seatA = 20
seatB = 15
seatC = 10


def main():
    a = int(input("Enter the number of tickets for A class sold: "))
    b = int(input("Enter the number of tickets for B class sold: "))
    c = int(input("Enter the number of tickets for C class sold: "))
    print("The amount of income generated from ticket sales, UAH:", format(incomeTotal(a, b, c), '.2f'))


def incomeA(a):
    incomeA = a * seatA
    return incomeA


def incomeB(b):
    incomeB = b * seatB
    return incomeB


def incomeC(c):
    incomeC = c * seatC
    return incomeC


def incomeTotal(a, b, c):
    incomeTotal = incomeA(a) + incomeB(b) + incomeC(c)
    return incomeTotal


main()
