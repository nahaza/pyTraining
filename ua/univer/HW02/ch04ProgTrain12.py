# 12. Calculating the Factorial of a Number
# In mathematics, the notation n! represents the factorial of the nonnegative integer n. The
# factorial of n is the product of all the nonnegative integers from 1 to n. For example,
# 7! 5 1 3 2 3 3 3 4 3 5 3 6 3 7 5 5,040
# and
#  4! 5 1 3 2 3 3 3 4 5 24
# Write a program that lets the user enter a nonnegative integer then uses a loop to calculate
# the factorial of that number. Display the factorial.

num = int(input("Enter a nonnegative integer: "))
factorial = 1
while num >= 0:
    for i in range(1, num+1):
        factorial *= i
    print(num, "!= ", factorial)
    num = int(input("Enter a nonnegative integer: "))
    print("Warning: it is not a nonnegative integer. Enter a nonnegative integer")