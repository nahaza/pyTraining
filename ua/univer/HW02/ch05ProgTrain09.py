# 9. Monthly Sales Tax
# A retail company must file a monthly sales tax report listing the total sales for the month,
# and the amount of state and county sales tax collected. The state sales tax rate is 5 percent
# and the county sales tax rate is 2.5 percent. Write a program that asks the user to enter
# the total sales for the month. From this figure, the application should calculate and display
# the following:
# • The amount of county sales tax
# • The amount of state sales tax
# • The total sales tax (county plus state)

taxFederalRate = 0.05
taxRegionRate = 0.025


def main():
    purchase = float(input("Enter the purchase amount, UAH: "))
    taxFederal = getTaxFederal(purchase)
    taxRegion = getTaxRegion(purchase)
    totalTax = getTotalTax(purchase)
    print('Purchase amount, UAH: ', format(purchase, '.2f'))
    print("Federal tax, UAH:", format(taxFederal, '.2f'))
    print("Region tax, UAH:", format(taxRegion, '.2f'))
    print("Total tax amount, UAH:", format(totalTax, '.2f'))


def getTaxFederal(purchase):
    return taxFederalRate * purchase


def getTaxRegion(purchase):
    return taxRegionRate * purchase


def getTotalTax(purchase):
    return getTaxFederal(purchase) + getTaxRegion(purchase)


main()
