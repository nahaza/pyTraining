# 3. Line Numbers
# Write a program that asks the user for the name of a file. The program should display the
# contents of the file with each line preceded with a line number followed by a colon. The
# line numbering should start at 1.

def main():
    fileName = input("Enter the name of the file: ")
    contentFile = open(fileName, 'r')
    content = contentFile.readline()
    lineCount = 1
    while content != '':
        print(str(lineCount)+":", content.rstrip('\n'))
        content = contentFile.readline()
        lineCount += 1
    contentFile.close()


if __name__ == '__main__':
    main()
