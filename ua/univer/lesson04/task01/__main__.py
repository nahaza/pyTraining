# 1. считать с консоли 6 числовых значений и записать в файл.
# 2. прочитать из файла значения и записать в список, посчитать сумму и среднее
# 3. 1 и 2 сделать для матрицы(2х3)


def write_mas_to_file(mas, filename="mas.txt"):
    with open("mas.txt", "w") as myfile:
        for value in mas:
            myfile.write(str(value))
            myfile.write("\n")


def write_mas_to_file_in_row(mas, filename="mas.txt"):
    with open("mas.txt", "w") as myfile:
        for value in mas:
            myfile.write(str(value))
            myfile.write(" ")


def read_mas_from_file(filename="mas.txt"):
    mas=[]
    with open("mas.txt", "r") as myfile:
        for line in myfile:
            mas.append(int(line))
    return mas


def read_mas_from_file(filename="mas.txt"):
    mas=[]
    with open("mas.txt", "r") as myfile:
        for line in myfile:
            words = line.strip()
            line.split()
            mas.append(int(line))
    return mas


if __name__ == '__main__':
    mas = [1,2,3,4,5,6]
    write_mas_to_file_in_row(mas, "mas_row.txt")
#    mas1=read_mas_from_file()
#    print(mas1)
#    print(sum(mas1))
#    print(sum(mas1)/len(mas1))
    matrix = [
        [1,1,1],
        [2,2,2]
    ]
    with open(("matrix.txt", "w")) as myfile:
        for row in matrix:
            for cell in row:
                myfile.write(str(cell))
                myfile.write((" "))
            myfile.write("\n")

    matrix1 = []
    with open(("matrix.txt", "r")) as myfile:
        for row in myfile:
            row
            matrix1.append((list())
            words = line.strip().split(" ")
            for word in words:
                row.append

