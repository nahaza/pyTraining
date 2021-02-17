# recipe
cookiesBase = 48
sugarBase = 1.5
butterBase = 1
flourBase = 2.75
cookiesToMake = int(input("Enter the number of cookies to make: "))
cookiesRatio = cookiesToMake / cookiesBase
sugarTotal = sugarBase * cookiesRatio
butterTotal = butterBase * cookiesRatio
flourTotal = flourBase * cookiesRatio
print("The amount of sugar, cups: ", format(sugarTotal, '.2f'))
print("The amount of butter, cups: ", format(butterTotal, '.2f'))
print("The amount of flour, cups: ", format(flourTotal, '.2f'))