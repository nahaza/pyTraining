# 7. Программа записи файла со случайными числами. Напишите программу, которая
# пишет в файл ряд случайных чисел. Каждое случайное число должно быть в диапазоне
# от 1 до 500. Приложение должно предоставлять пользователю возможность назначать
# количество случайных чисел, которые будут содержаться в файле.

import random

def getNumRand():
    numRand = random.randint(1, 500)
    return numRand


def main():
    lineNum = int(input("Enter the number of random numbers: "))
    toFile = open("numbers7.txt", 'a')
    num = 0
    for x in range(1, lineNum+1):
        numRan = getNumRand()
        toFile.write(str(numRan)+'\n')
    toFile.close()
    print("Updated")


if __name__ == '__main__':
    main()