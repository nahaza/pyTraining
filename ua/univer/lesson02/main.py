# 1. Даны 4 числа типа int. Сравнить их и вывести наименьшее на консоль.
# 2. Вывести на консоль количество максимальных чисел среди этих четырех.

def findMin(x, y):
    if x < y:
        return x
    else:
        return y


def printMin(x, y):
    if x < y:
        myMin = x
    else:
        myMin = y
    print(myMin)


a = 2
b = 1
c = 3
d = 3

minLoc = findMin(findMin(a, b), findMin(c, d))

print(minLoc)
