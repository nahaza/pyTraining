# 6. File Analysis
# Write a program that reads the contents of two text files and compares them in the following ways:
# • It should display a list of all the unique words contained in both files.
# • It should display a list of the words that appear in both files.
# • It should display a list of the words that appear in the first file but not the second.
# • It should display a list of the words that appear in the second file but not the first.
# • It should display a list of the words that appear in either the first or second file, but not
# both.
# Hint: Use set operations to perform these analyses.

def getWordList(file):
    fromFile = open(file, 'r')
    dataFile = fromFile.read()
    wordList = dataFile.replace('.', '')
    wordList = wordList.lower()
    wordList = set(wordList.split(' '))
    fromFile.close()
    return wordList


def getDataForDiscrepancies(file1, file2):
    wordList1 = getWordList(file1)
    wordList2 = getWordList(file2)
    uniqueWordsInBoth = wordList1.union(wordList2)
    sameWordsInBoth = wordList1.intersection(wordList2)
    uniqueWordsInFile1 = wordList1.difference(wordList2)
    uniqueWordsInFile2 = wordList2.difference(wordList1)
    uniqueWordsFromBoth = wordList1.symmetric_difference(wordList2)
    return uniqueWordsInBoth, sameWordsInBoth, uniqueWordsInFile1, uniqueWordsInFile2, uniqueWordsFromBoth


def main():
    file1 = 'text1ForTask06.txt'
    file2 = 'text2ForTask06.txt'
    uniqueWordsInBoth, sameWordsInBoth, uniqueWordsInFile1, \
    uniqueWordsInFile2, uniqueWordsFromBoth = getDataForDiscrepancies(file1, file2)
    print("List of all the unique words contained in both files: ", '\n')
    for x in uniqueWordsInBoth:
        print(x)
    print()
    print("List of the words that appear in both files: ", '\n')
    for x in sameWordsInBoth:
        print(x)
    print()
    print("List of the words that appear in the first file but not the second: ", '\n')
    for x in uniqueWordsInFile1:
        print(x)
    print()
    print("List of the words that appear in the second file but not the first: ", '\n')
    for x in uniqueWordsInFile2:
        print(x)
    print()
    print("List of the words that appear in either the first or second file, but not both: ", '\n')
    for x in uniqueWordsFromBoth:
        print(x)


if __name__ == '__main__':
    main()
