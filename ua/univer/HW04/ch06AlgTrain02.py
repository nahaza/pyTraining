# 2. Напишите программу, которая открывает файл my_name.txt, созданный программой в задаче 1, читает ваше имя
# из файла, выводит имя на экран и затем закрывает файл.

def readMyName():
    fromFile = open("MyName.txt", 'r')
    print(fromFile.readline())
    fromFile.close()


def main():
    readMyName()


if __name__ == '__main__':
    main()
