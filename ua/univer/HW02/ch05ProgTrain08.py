# 8. Оценщик малярных работ. Малярная компания установила,
# что на каждые 10 квадратных метров поверхности стены требуется 5 литров краски и 8 часов работы.
# Компания взимает за работу 2000 руб. в час. Напишите программу, которая просит пользователя
# ввести площадь поверхности окрашиваемой стены и цену 5-литровой емкости краски.
# Программа должна показать следующие данные:
# • количество требующихся емкостей краски;
# • количество требующихся рабочих часов;
# • стоимость краски;
# • стоимость работы;
# • общая стоимость малярных работ


hoursRate = 8
laborChargePerHour = 2000
squareRate = 10


def main():
    square = float(input("Enter the square of wall space to be painted, sq m: "))
    paintPrice = float(input("Enter the price of the 5-l tin of paint, UAH: "))
    print("The number of tins of paint required:", getNumberTins(square))
    print("The hours of labor required:", getHourLabor(square))
    print("The cost of the paint, UAH:", format(getPaintCost(square, paintPrice), '.2f'))
    print("The labor charges, UAH:", format(getLaborCost(square), '.2f'))
    print("The total cost of the paint job, UAH:", format(totalCost(square, paintPrice), '.2f'))


def getNumberTins(square):
    numberTins = square / squareRate
    if square % squareRate != 0:
        numberTins = int(format((square / squareRate + 1), '.0f'))
    else:
        numberTins = square // squareRate
    return numberTins


def getPaintCost(square, paintPrice):
    paintCost = getNumberTins(square) * paintPrice
    return paintCost


def getHourLabor(square):
    if square % squareRate != 0:
        hourLabor = int((square / squareRate + 1) * hoursRate)
    else:
        hourLabor = square // squareRate * hoursRate
    return hourLabor


def getLaborCost(square):
    laborCost = getHourLabor(square) * laborChargePerHour
    return laborCost


def totalCost(square, paintPrice):
    totalCost = getPaintCost(square, paintPrice) + getLaborCost(square)
    return totalCost


main()