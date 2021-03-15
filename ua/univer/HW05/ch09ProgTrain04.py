# 4. Unique Words
# Write a program that opens a specified text file then displays a list of all the unique words
# found in the file.
# Hint: Store each word as an element of a set.

def main():
    fileWithWords = open('textForTask03.txt', 'r')
    dataFromFile = fileWithWords.read()
    print(dataFromFile)
    fileWithWords.close()
    uniqueWords = set(dataFromFile.split())
    print(uniqueWords)


if __name__ == '__main__':
    main()