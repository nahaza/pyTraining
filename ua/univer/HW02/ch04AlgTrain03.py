# Напишите цикл for, который выводит приведенный ниже ряд чисел:
# О, 10, 20, 30, 40, 50, ... , 1000
r = 0
for r in range(-1, 1001, 10):
    print(r)

# Write a for loop that uses the range function to display all odd numbers between
# 1 and 100.
r = 0
for r in range(1, 101):
    if r % 2 != 0:
        print(r)
