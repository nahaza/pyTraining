# 10. Feet to Inches
# One foot equals 12 inches. Write a function named feet_to_inches that accepts a number
# of feet as an argument and returns the number of inches in that many feet. Use the function
# in a program that prompts the user to enter a number of feet then displays the number of
# inches in that many feet.

footToInches = 12


def main():
    feet = int(input("Enter a number of feet: "))
    inches = feetToInches(feet)
    print("The number of inches in", feet, "feet =", inches)


def feetToInches(feet):
    numberOfInches = feet * footToInches
    return numberOfInches


main()
