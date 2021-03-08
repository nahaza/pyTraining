# 8. Sentence Capitalizer
# Write a program with a function that accepts a string as an argument and returns a copy
# of the string with the first character of each sentence capitalized. For instance,
# if the argument is “hello. my name is Joe. what is your name?” the function should return the string
# “Hello. My name is Joe. What is your name?” The program should let the user enter
# a string and then pass it to the function. The modified string should be displayed.


def toBeginWithUpper(string):
    punctuation = []
    for i in range(len(string)):
        if string[i] == '.':
            punctuation.append('.')
        elif string[i] == '?':
            punctuation.append('?')
        elif string[i] == '!':
            punctuation.append('!')
    string = string.replace('?', '.').replace('!', '.')
    sentences = string.split('.')
    while '' in sentences:
        sentences.remove('')
    myList = []
    for i in range(len(sentences)):
        sentences[i] = sentences[i].lstrip(' ')
        sentences[i] = sentences[i][0].upper() + sentences[i][1:]
    newString = ''
    for i in range(len(sentences)):
        newString += sentences[i]
        newString += punctuation[i] + ' '
    newString = newString[:-1]
    return newString


def main():
    myString = input('Enter your sentences: ')
    print(toBeginWithUpper(myString))


if __name__ == '__main__':
    main()
