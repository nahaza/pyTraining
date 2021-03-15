# 3. Шифрование и дешифрование файлов. Напишите программу, которая применяет словарь для присвоения "кодов"
# каждой букве алфавита. Например:
# codes = { , А, : , % , , , а, : , 9 ,, , Б, : , @,, , 6 , : , #, ... }
# Здесь букве А присвоен символ %, букве а - число 9, букве Б - символ @ и т. д. Программа должна открыть
# заданный текстовый файл, прочитать его содержимое и применить словарь для записи зашифрованной версии содержимого
# файла во второй файл. Глава 9. Словари и множества 509
# Каждый символ во втором файле должен содержать код для соответствующего символа
# из первого файла.
# Напишите вторую программу, которая открывает зашифрованный файл и показывает его
# дешифрованное содержимое на экране.
def getDictEncrypt():
    dictEncrypt = {
        'A': '!', 'B': '@', 'C': '#', 'D': '$', 'E': '%', 'F': '^', 'G': '&', 'H': '*', 'I': '(',
        'J': ')', 'K': '-', 'L': '_', 'M': '+', 'N': '=', 'O': '`', 'P': '~', 'Q': '{', 'R': '[',
        'S': '}', 'T': ']', 'U': ':', 'V': ';', 'W': '"', 'X': '<', 'Y': '>', 'Z': '0', 'a': '1',
        'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': 'a',
        'k': 'b', 'l': 'c', 'm': 'd', 'n': 'e', 'o': 'f', 'p': 'g', 'q': 'h', 'r': 'i', 's': 'j',
        't': 'k', 'u': 'l', 'v': 'm', 'w': 'n', 'x': 'o', 'y': 'p', 'z': 'q'}
    decryptKeyValues = dictEncrypt.items()
    return dictEncrypt, decryptKeyValues


def doEncrypt(dictEncrypt, fileToEncrypt, fileToDecrypt):
    dataFromFileToEncrypt = open(fileToEncrypt, 'r')
    dataToEncrypt = dataFromFileToEncrypt.read()
    dataFromFileToEncrypt.close()
    encryptedFile = open(fileToDecrypt, 'a')
    for x in dataToEncrypt:
        if x in dictEncrypt:
            encryptedFile.write(dictEncrypt[x])
        else:
            encryptedFile.write(x)
    encryptedFile.close()


def doDecrypt(dictEncrypt, fileToDecrypt, decryptKeyValues):
    dataFromFileToDecrypt = open(fileToDecrypt, 'r')
    dataToDecrypt = dataFromFileToDecrypt.read()
    dataFromFileToDecrypt.close()
    for y in dataToDecrypt:
        if y not in dictEncrypt.values() or y == '.' or y == ',' or y == ' ':
            print(y, end='')
        else:
            for k, v in decryptKeyValues:
                if y == v and y != '.':
                    print(k, end='')
    print()


def main():
    dictEncrypt, decryptKeyValues = getDictEncrypt()
    fileToEncrypt = "textForTask03.txt"
    fileToDecrypt = "encrypted.txt"
    doEncrypt(dictEncrypt, fileToEncrypt, fileToDecrypt)
    doDecrypt(dictEncrypt, fileToDecrypt, decryptKeyValues)


if __name__ == '__main__':
    main()
