# Compound Interest
P = float(input("Enter the amount of principal originally deposited into the account, UAH: "))
r = float(input("Enter the annual interest rate paid by the account, %: "))
n = int(input("Enter the number of times per year that the interest is compounded: "))
t = int(input("Enter the  number of years the account will be left to earn interest, years: "))
#  the amount of money in the account after the specified number of years
r /= 100
A = P * ((1 + r/n) ** (n * t))
print("The amount of money in the account after the specified number of years, UAH:",
      format(A, '.2f'))
