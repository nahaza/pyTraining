# 4. Даны имена 2х человек (тип string). Если имена равны,
# 	то вывести сообщение о том, что люди являются тезками.

def task04_compare_2_human(name1, name2):
    if name1 == name2:
        print("They have the same name")
    else:
        print("They have different names")


name1 = str(input("Enter name#1: "))
name2 = str(input("Enter name#2: "))

task04_compare_2_human(name1, name2)
