# 8. Имена и адреса электронной почты. Напишите программу, которая сохраняет имена и
# адреса электронной почты в словаре в виде пар ключ/значение. Программа должна вывести меню,
# которое позволяет пользователю отыскать адрес электронной почты человека,
# добавить новое имя и адрес электронной почты, изменить существующий адрес электронной почты
# и удалить существующее имя и адрес электронной почты. Программа
# должна законсервировать словарь и сохранить его в файле при выходе пользователя из
# программы. При каждом запуске программы она должна извлечь словарь из файла и его
# расконсервировать.

import pickle
import os


def main():
    if not os.path.isfile('DictionNamesEmails.txt'):
        fromFile = open('DictionNamesEmails.txt', 'wb')
        email = {}
        newDict = {}
        name = input('Enter a name: ').lower()
        email[name] = input('Enter email: ')
        pickle.dumps(email, fromFile)
        fromFile.close()
        main()
    else:
        fromFile = open('DictionNamesEmails.txt', 'rb')
        email = getDictEmail(fromFile)
        fromFile.close()
        again = 'y'
        while again.lower() == 'y':
            print('MENU')
            print('1. To add new name and email')
            print('2. Change the email')
            print('3. Delete the email')
            print('4. Display the email')
        anyChange = False
        userChoice = int(input('Make a choice: '))
        if userChoice == 1:
            newDict = toAddNew(email)
            anyChange = True
        elif userChoice == 2:
            newDict = toChange(email)
            anyChange = True
        elif userChoice == 3:
            newDict = toDelete(email)
            anyChange = True
        elif userChoice == 4:
            toDisplay(email)
        else:
            print("Make the correct choice")
        again = input("Enter y as yes to continue: ")
        tempFile = open('temp.txt', 'wb')
        newDict = {}
        if anyChange:
            pickle.dump(newDict, tempFile)
            tempFile.close()
            os.remove('DictionNamesEmails.txt')
            os.rename('temp.txt', 'DictionNamesEmails.txt')
        print("Updated and saved")
        fromFile.close()


def getDictEmail(fromFile):
    dictEmail = pickle.load(fromFile)
    return dictEmail


def toAddNew(email):
    name = input("Enter a new name: ")
    if name.lower() not in email:
        email[name.lower()] = input("Enter email: ")
        print('Saved')
    else:
        print('The named is already in a database')
    return email


def toChange(email):
    name = input("Enter the name to change email: ")
    if name.lower() in email:
        email[name.lower()] = input("Enter new email: ")
        print('Saved')
    else:
        print('The named is not in a database')
    return email


def toDelete(email):
    name = input("Enter the name to delete email: ")
    if name.lower() in email:
        del email[name.lower()]
        print('Saved')
    else:
        print('The named is not in a database')
    return email


def toDisplay(email):
    try:
        name = input("Enter the name to change email: ")
        print(email[name.lower()])
    except KeyError:
        print('The name is not found')


if __name__ == '__main__':
    main()
