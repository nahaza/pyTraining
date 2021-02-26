# 6. Больше числа п. В программе напишите функцию, которая принимает два аргумента:
# список и число п. Допустим, что список содержит числа. Функция должна показать все
# числа в списке, которые больше п.

def main():
    numList = [45, 78, 96, 46, 1]
    number = int(input("Enter a number: "))
    moreThanNumber(numList, number)


def moreThanNumber(numList, number):
    for x in numList:
        if x > number:
            print(x)


main()
