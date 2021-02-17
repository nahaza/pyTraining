# Shipping Charges
weightOfPackage = float(input("Enter the weight of a package, g: "))
if weightOfPackage < 0:
    print("Enter the valid weight of the package")
else:
    if 0 < weightOfPackage <= 200:
        ratePerGram = 1.50
    elif 200 < weightOfPackage <= 600:
        ratePerGram = 3.00
    elif 600 < weightOfPackage <= 1000:
        ratePerGram = 4.00
    else:
        ratePerGram = 4.75
    shippingCharges = weightOfPackage * ratePerGram
    print("The shipping charges, UAH:", format(shippingCharges, '.2f'))
