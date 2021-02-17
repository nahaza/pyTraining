# Hot Dog Cookout Calculator
numberOfPeople = int(input("Enter the number of people attending the cookout: "))
hotdogsPerPerson = int(input("Enter the number of hot dogs each person will be given: "))
totalHotdogs = numberOfPeople * hotdogsPerPerson
sausagesInPackage = 10
bunsInPackage = 8
if totalHotdogs % sausagesInPackage > 0:
    numberOfSausagesPackage = (totalHotdogs // sausagesInPackage) + 1
else:
    numberOfSausagesPackage = totalHotdogs // sausagesInPackage
if totalHotdogs % bunsInPackage > 0:
    numberOfBunsPackage = (totalHotdogs // bunsInPackage) + 1
else:
    numberOfBunsPackage = totalHotdogs // bunsInPackage
numberOfSausagesLeft = (numberOfSausagesPackage * sausagesInPackage) % totalHotdogs
numberOfBunsLeft = (numberOfBunsPackage * bunsInPackage) % totalHotdogs
print("The minimum number of packages of sausages required:", numberOfSausagesPackage)
print("The minimum number of packages of buns required:", numberOfBunsPackage)
if numberOfSausagesLeft > 0:
    print("The number of sausages that will be left over:", numberOfSausagesLeft)
if numberOfBunsLeft > 0:
    print("The number of buns that will be left over:", numberOfBunsLeft)
