# 8. Программа чтения файлов со случайными числами. Выполнив предыдущее задание
# (программу записи файла со случайными числами), напишите еще одну программу,
# которая читает случайные числа из файла, выводит их на экран и затем показывает
# приведенные ниже данные:
# • сумму чисел;
# • количество случайных чисел, прочитанных из файла.


def main():
    numCount = 0
    total = 0
    fromFile = open('numbers7.txt', 'r')
    numb = fromFile.readline()
    while numb != '':
        numb = int(numb.rstrip('\n'))
        total += numb
        numCount += 1
        numb = fromFile.readline()
    fromFile.close()
    print("Total:", total)
    print("The number of random numbers in file:", numCount)


if __name__ == '__main__':
    main()
