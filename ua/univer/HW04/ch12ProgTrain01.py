# 1. Рекурсивная печать. Разработайте рекурсивную функцию, которая принимает целочисленный
# аргумент п и распечатывает числа от 1 до п.

#
def main():
    n = 1
    num = int(input("Enter positive number: "))
    printNum(n, num)


def printNum(n, num):
    print(n)
    if n <= num-1:
        printNum(n+1, num)


if __name__ == '__main__':
    main()
