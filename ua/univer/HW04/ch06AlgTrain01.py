# 1. Напишите программу, которая открывает файл вывода my_name.txt, пишет в него ваше
# имя и затем его закрывает.

def writeMyName(name):
    fromFile = open("MyName.txt", 'w')
    fromFile.write(name)
    fromFile.close()


def main():
    name = input("Enter your name: ")
    writeMyName(name)


if __name__ == '__main__':
    main()
