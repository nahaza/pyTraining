# 6. Average Number of Words
# If you have downloaded the source code from the Premium Companion Website you will
# find a file named text.txt in the Chapter 08 folder. The text that is in the file is stored
# as one sentence per line. Write a program that reads the file’s contents and calculates the
# average number of words per sentence.

def main():
    totalWords = 0
    grandTotalWords = 0
    fromFile = open('text.txt', 'r')
    textList = fromFile.read()
    sentList = textList.split('.')
    for sent in sentList:
        wordList = sent.split(' ')
        for word in wordList:
            totalWords += 1
    grandTotalWords += totalWords
    averNumbWords = grandTotalWords / len(sentList)
    print(format(averNumbWords, '.0f'))
    fromFile.close()


main()
