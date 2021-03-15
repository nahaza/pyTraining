# 3. Assume the variable dct references a dictionary. Write an if statement that determines whether the
# key 'James' exists in the dictionary. If so, display the value that
# is associated with that key. If the key is not in the dictionary, display a message
# indicating so.

findJames = dct.get('James', 'James is not in the dictionary')
print(findJames)

# 3. Предположим, что переменная dct ссылается на словарь. Напишите инструкцию if, которая определяет,
# существует ли в словаре ключ 'Джеймс'. Если да, то покажите значение, которое связано с этим ключом.
# Если ключа в словаре нет, то покажите соответствующее сообщение.

if 'James' in dct:
    print(dct['James'])
