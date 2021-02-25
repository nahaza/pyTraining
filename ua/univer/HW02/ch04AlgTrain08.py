# 8. Write code that prompts the user to enter a positive nonzero number and validates
# the input.

num = int(input("Enter a positive nonzero number: "))
while num <= 0:
    print("Warning: it is not a positive nonzero number")
    num = int(input("Enter a positive nonzero number: "))
