# Software Sales
numberOfPackages = int(input("Enter the number of packages purchased: "))
quantityAGradeMin = 0
quantityAGradeMax = 9
quantityBGradeMin = 10
quantityBGradeMax = 19
quantityCGradeMin = 20
quantityCGradeMax = 49
quantityDGradeMin = 50
quantityDGradeMax = 99
quantityEGradeMin = 100
discountA = 0
discountB = 0.1
discountC = 0.2
discountD = 0.3
discountE = 0.4
packagePrice = 9.99
totalBeforeDiscount = numberOfPackages * packagePrice
if numberOfPackages < quantityAGradeMin:
    print("Warning, enter the valid number of packages.")
else:
    if quantityAGradeMin <= numberOfPackages <= quantityAGradeMax:
        discount = discountA
    elif quantityBGradeMin <= numberOfPackages <= quantityBGradeMax:
        discount = discountB
    elif quantityCGradeMin <= numberOfPackages <= quantityCGradeMax:
        discount = discountC
    elif quantityDGradeMin <= numberOfPackages <= quantityDGradeMax:
        discount = discountD
    else:
        discount = discountE
    discountAmount = totalBeforeDiscount * discount
    totalAfterDiscount = totalBeforeDiscount - discountAmount
    print("Your discount is " + format(discountAmount, '.2f') +
          " UAH and total amount of the purchase after the discount is " +
          format(totalAfterDiscount, '.2f') + " UAH")
