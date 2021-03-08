# 2. File Head Display
# Write a program that asks the user for the name of a file. The program should display only
# the first five lines of the file’s contents. If the file contains less than five lines, it should
# display the file’s entire contents.

def main():
    linesToRead = 5
    lineCount = 0
    fileName = input("Enter the name of the file: ")
    contentFile = open(fileName, 'r')
    content = contentFile.readline()
    lineCount += 1
    while content != '' and lineCount <= linesToRead:
        print(content.rstrip('\n'))
        content = contentFile.readline()
        lineCount += 1
    contentFile.close()


if __name__ == '__main__':
    main()
