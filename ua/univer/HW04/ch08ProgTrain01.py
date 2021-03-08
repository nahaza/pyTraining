# 1. Инициалы. Напишите программу, которая получает строковое значение, содержащее
# имя, отчество и фамилию человека и показывает инициалы. Например, если пользователь
# вводит Михаил Иванович Кузнецов, то программа должна вывести М.И.К.


def inputName():
    name = input("Enter your name: ")
    return name


def splitName(name):
    nameList = name.split(' ')
    return nameList


def initials(nameList):
    return (nameList[0][0] + "." + nameList[1][0] + "." + nameList[2][0]).upper()


def main():
    name = inputName()
    nameList = splitName(name)
    initialName = initials(nameList)
    print(initialName)
    print(nameList[0][0].upper(), nameList[1][0].upper(), nameList[2][0].upper(), sep='.')


if __name__ == '__main__':
    main()
