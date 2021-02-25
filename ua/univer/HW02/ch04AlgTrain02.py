# Write a while loop that asks the user to enter two numbers. The numbers should be
# added and the sum displayed. The loop should ask the user if he or she wishes to
# perform the operation again. If so, the loop should repeat, otherwise it should terminate

keepOn = 'Y'
print("This program is supposed to add up two numbers")
while keepOn == 'Y' or keepOn == 'y':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sumNum = num1 + num2
    print("The sum is:", sumNum)
    keepOn = input("Do you want to continue? Enter Y for 'yes': ")
print("Finish")
