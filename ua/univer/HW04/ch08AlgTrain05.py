# 5. Напишите функцию, которая принимает строковое значение в качестве аргумента и возвращает истину, если аргумент
# заканчивается подстрокой ' . com'. В противном случае
# функция должна вернуть ложь.

def main():
    myString = input("Enter your string: ")
    if myString.endswith(".com"):
        return True
    else:
        return False


if __name__ == '__main__':
    main()



