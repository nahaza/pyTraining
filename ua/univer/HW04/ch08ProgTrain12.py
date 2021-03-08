# 12. Pig Latin
# Write a program that accepts a sentence as input and converts each word to “Pig Latin.” In
# one version, to convert a word to Pig Latin, you remove the first letter and place that letter
# at the end of the word. Then, you append the string “ay” to the word. Here is an example:
# English: I SLEPT MOST OF THE NIGHT
# Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY


def pigLatin(myString):
    words = myString.split()
    newWords = list()
    for i in words:
        newWord = i[1:] + i[0]+'AY'
        newWords.append(newWord)
    newSent = ' '.join(newWords)
    print(newSent)


def main():
    myString = input("Enter your string: ")
    pigLatin(myString)


if __name__ == '__main__':
    main()
