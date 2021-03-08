# 3. Напишите программу, которая делает следующее: открывает выходной файл с именем
# number_list.txt, применяет цикл для записи в файл чисел с 1 по 100, а затем закрывает
# файл.


def writeNumbers():
    fromFile = open("number_list.txt", 'w')
    for num in range(1, 101):
        fromFile.write(str(num)+'\n')
    fromFile.close()


def main():
    writeNumbers()


if __name__ == '__main__':
    main()
