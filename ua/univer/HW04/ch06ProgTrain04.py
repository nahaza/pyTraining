# 4. Счетчик значений. Допустим, что файл с серией имен (в виде строковых значений)
# называется names.txt и существует на диске компьютера. Напишите программу, которая
# показывает количество хранящихся в файле имен. (Подсказка: откройте файл и прочитайте каждую хранящуюся в нем строку. Примените переменную для подсчета количества прочитанных из файла значений.)


def main():
    contentFile = open('girls.txt', 'r')
    lineCount = 0
    content = contentFile.readline()
    while content != '':
        lineCount += 1
        content = contentFile.readline()
    print(lineCount)
    contentFile.close()


if __name__ == '__main__':
    main()