# 5. Charge Account Validation
# If you have downloaded the source code from the Premium Companion Website you will
# find a file named charge_accounts.txt in the Chapter 07 folder. This file has a list of a
# company’s valid charge account numbers. Each account number is a seven-digit number,
# such as 5658845.
# Write a program that reads the contents of the file into a list. The program should then
# ask the user to enter a charge account number. The program should determine whether
# the number is valid by searching for it in the list. If the number is in the list, the program
# should display a message indicating the number is valid. If the number is not in the list, the
# program should display a message indicating the number is invalid.

def openFile(file):
    ch7file = open('charge_accounts.txt', 'r')
    accountNumbers = ch7file.readlines()
    ch7file.close()
    return accountNumbers


def listNumbers(accounts):
    for x in range(0, len(accounts)):
        accounts[x] = accounts[x].rstrip('\n')
    return accounts


def inputChoice():
    return input('Enter a charge account number: ')


def results(accNum, accounts):
    return accNum in accounts


def printResults(accNum, result):
    if result:
        print(accNum, 'number is valid')
    else:
        print(accNum, 'number is not in the list')


def main():
    file = openFile('charge_accounts.txt')
    accountList = listNumbers(file)
    accountNumber = inputChoice()
    result = results(accountNumber, accountList)
    printResults(accountNumber, result)


main()