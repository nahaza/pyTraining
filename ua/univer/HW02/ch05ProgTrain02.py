# 2. Модернизация программы расчета налога с продаж. В задаче 6 по программированию
# из главы 2 рассматривалась программа расчета налога с продаж. Требовалось написать
# программу, которая вычисляет и показывает региональный и федеральный налоги с продаж, взимаемые при покупке.
# Если эта программа уже вами написана, модернизируйте ее
# так, чтобы подзадачи были помещены в функции. Если вы ее еще не написали, то напишите с использованием функций.

taxFederalRate = 0.05
taxRegionRate = 0.0025

def main():
    purchase = float(input("Enter the purchase amount, UAH: "))
    print('Purchase amount, UAH: ', format(purchase, '.2f'))
    print("Federal tax, UAH:", format(taxFederal(purchase), '.2f'))
    print("Region tax, UAH:", format(taxRegion(purchase), '.2f'))
    print("Total tax amount, UAH:", format(totalTax(purchase), '.2f'))
    print("Total purchase, UAH:", format(purchaseTotal(purchase), '.2f'))


def taxFederal(purchase):
    taxFederal = taxFederalRate * purchase
    return taxFederal


def taxRegion(purchase):
    taxRegion = taxRegionRate * purchase
    return taxRegion


def totalTax(purchase):
    totalTax = taxFederal(purchase) + taxRegion(purchase)
    return totalTax


def purchaseTotal(purchase):
    purchaseTotal = purchase + totalTax(purchase)
    return purchaseTotal


main()
