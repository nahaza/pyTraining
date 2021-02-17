# total sales
taxRateFromSales = 0.07
item1price = float(input("Enter the price of item 1, UAH: "))
item2price = float(input("Enter the price of item 2, UAH: "))
item3price = float(input("Enter the price of item 3, UAH: "))
item4price = float(input("Enter the price of item 4, UAH: "))
item5price = float(input("Enter the price of item 5, UAH: "))
totalNetRevenue = item1price + item2price + item3price + item4price + item5price
taxFromSales = totalNetRevenue * taxRateFromSales
totalRevenue = totalNetRevenue + taxFromSales
print("Net Revenue, UAH: ", format(totalNetRevenue, '.2f'))
print("Tax from Sales, UAH: ", format(taxFromSales, '.2f'))
print("Total Revenue, UAH: ", format(totalRevenue, '.2f'))
