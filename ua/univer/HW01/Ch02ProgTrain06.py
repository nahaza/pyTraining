# purchase, taxes
purchase = float(input("Enter the purchase amount, UAH: "))
taxFederalRate = 0.05
taxRegionRate = 0.0025
taxFederal = taxFederalRate * purchase
taxRegion = taxRegionRate * purchase
totalTax = taxFederal + taxRegion
purchaseTotal = purchase + totalTax
print('Purchase amount, UAH: ', format(purchase, '.2f'))
print("Federal tax, UAH:", format(taxFederal, '.2f'))
print("Region tax, UAH:", format(taxRegion, '.2f'))
print("Total tax amount, UAH:", format(totalTax, '.2f'))
print("Total purchase, UAH:", format(purchaseTotal, '.2f'))
