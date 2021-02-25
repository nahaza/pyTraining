# 13. Maximum of Two Values
# Write a function named max that accepts two integer values as arguments and returns the
# value that is the greater of the two. For example, if 7 and 12 are passed as arguments to
# the function, the function should return 12. Use the function in a program that prompts the
# user to enter two integer values. The program should display the value that is the greater
# of the two.

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    numMax = maxim(num1, num2)
    if num1 == num2:
        print("These numbers are the same")
    else:
        print("The value that is the greater of the two:", numMax)


def maxim(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


main()
