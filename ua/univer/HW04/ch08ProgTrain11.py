# 11. Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together,
# but the first character of each word is uppercase. Convert the sentence to a string in which
# the words are separated by spaces, and only the first word starts with an uppercase letter. For
# example the string “StopAndSmellTheRoses.” would be converted to “Stop and smell
# the roses.”

def main():
    myString = input("Enter your string: ")
    newString = myString[0]
    for i in range(1, len(myString)):
        if myString[i].isupper():
            newString += ' '
            newString += myString[i].lower()
        else:
            newString += myString[i]
    print(newString)


if __name__ == '__main__':
    main()
