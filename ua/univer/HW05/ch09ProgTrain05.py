# 5. Частотность слов. Напишите программу, которая считывает содержимое текстового
# файла. Она должна создать словарь, в котором ключами являются отдельные слова
# в файле, и значениями - количество появлений каждого слова. Например, если слово
# 'это' появляется 128 раз, то словарь должен содержать элемент с ключом 'это' и
# значeнием 128. Программа должна либо показать частотность каждого слова, либо создать
# второй файл, содержащий список слов и их частотностей.

import pickle


def main():
    fileToMakeDict = open('textForTask05.txt', 'r')
    dataForDict = fileToMakeDict.read()
    dataForDict = dataForDict.replace(".", "")
    wordList = list(dataForDict.split(" "))
    wordCount = {}
    for word in wordList:
        if word not in wordCount:
            wordCount.update({word: 1})
        else:
            wordCount[word] += 1
    print(wordCount)
    dictItself = open('wordDict.txt', 'wb')
    pickle.dump(wordCount, dictItself)
    fileToMakeDict.close()
    dictItself.close()


if __name__ == '__main__':
    main()
