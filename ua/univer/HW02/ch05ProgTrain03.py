# 3. How Much Insurance?
# Many financial experts advise that property owners should insure their homes or buildings
# for at least 80 percent of the amount it would cost to replace the structure. Write a program
# that asks the user to enter the replacement cost of a building, then displays the minimum
# amount of insurance he or she should buy for the property.

insurRate = 0.80

def main():
    replCost = float(input("Enter the replacement cost of a building. UAH: "))
    print("The minimum amount of insurance should be bought for the property, UAH:", format(insurance(replCost), '.2f'))


def insurance(replCost):
    insurance = replCost * insurRate
    return insurance


main()
