# charge for food, tip, tax
tipRate = 0.18
taxFromSalesRate = 0.07
chargeForFood = float(input("Enter charge for the food, UAH: "))
tipAmount: float = chargeForFood * tipRate
taxFromSales: float = chargeForFood * taxFromSalesRate
totalAmountInReceipt: float = chargeForFood + tipAmount + taxFromSales

print("Tip, UAH:", format(tipAmount, '.2f'))
print("Tax from sales, UAH:", format(taxFromSales, '.2f'))
print("Receipt total amount, UAH:", format(totalAmountInReceipt, '.2f'))

