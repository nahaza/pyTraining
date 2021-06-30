# 1. Даны 4 числа типа int. Сравнить их и вывести наименьшее на консоль.
# 2. Вывести на консоль количество максимальных чисел среди этих четырех.


import task_if_lib

a = 2
b = 1
c = 3
d = 3

task_if_lib.print_min(10, 20)

min_local = task_if_lib.find_min(task_if_lib.find_min(a, b), task_if_lib.find_min(c, d))
print("min=", min_local)

task_if_lib.find_and_print_max_count(a, b, c, d)
