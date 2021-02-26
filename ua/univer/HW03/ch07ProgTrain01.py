# 1. Общий объем продаж. Разработайте программу, которая просит пользователя ввести
# продажи магазина за каждый день недели. Суммы должны быть сохранены в списке.
# Примените цикл, чтобы вычислить общий объем продаж за неделю и показать результат.


def main():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    amount = []
    total = 0

    print("Enter sales for each day, UAH")
    for sales in days:
        sales = float(input(sales + ': '))
        amount.append(sales)

    for sales in amount:
        total += sales

    print("Total, UAH:", total)


main()
