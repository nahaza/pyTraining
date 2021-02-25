# 1. Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, then converts that
# distance to miles. The conversion formula is as follows:
# Miles 5 Kilometers 3 0.6214

def main():
    km = int(input("Enter the number of km: "))
    miles = kmToMl(km)
    print(km, "km =", miles, "ml")


def kmToMl(km):
    ml = km * 0.6214
    return format(ml, '.1f')


main()
