# men, women
numberOfMen = int(input("Enter the number of men: "))
numberOfWomen = int(input("Enter the number of women: "))
peopleTotal = numberOfMen + numberOfWomen
malePercentage = numberOfMen / peopleTotal
femalePercentage = numberOfWomen / peopleTotal
print("The percentage of men:", format(malePercentage, '.0%'))
print("The percentage of women:", format(femalePercentage, '.0%'))
