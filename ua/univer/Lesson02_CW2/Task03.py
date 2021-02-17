#  Даны 5 чисел (тип int). Вывести вначале наименьшее,
# а затем наибольшее из данных чисел.

def find_max(x, y):
    if x > y:
        return x
    else:
        return y


def find_min(x, y):
    if x < y:
        return x
    else:
        return y


def task03_print_5_min_max(a, b, c, d, e):
    maxAmong5 = find_max(find_max(find_max(a, b), find_max(c, d)), e)
    minAmong5 = find_min(find_min(find_min(a, b), find_min(c, d)), e)
    print("Maximum:", maxAmong5)
    print("Minimum:", minAmong5)


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))
e = int(input("Enter e: "))

task03_print_5_min_max(a, b, c, d, e)
