# 7. Character Analysis
# If you have downloaded the source code you will find a file named text.txt in the Chapter 08
# folder. Write a program that reads the file’s contents and determines the following:
# • The number of uppercase letters in the file
# • The number of lowercase letters in the file
# • The number of digits in the file
# • The number of whitespace characters in the file


def main():
    numUpper = 0
    numLower = 0
    numDigit = 0
    numSpace = 0
    fromFile = open('text.txt', 'r')
    textList = fromFile.read()
    for x in textList:
        if x.isupper():
            numUpper += 1
        elif x.islower():
            numLower += 1
        elif x.isdigit():
            numDigit += 1
        elif x.isspace():
            numSpace += 1
    print("The number of uppercase letters in the file: ", numUpper)
    print("The number of lowercase letters in the file: ", numLower)
    print("The number of digits in the file: ", numDigit)
    print("The number of whitespace characters in the file: ", numSpace)
    fromFile.close()


main()
