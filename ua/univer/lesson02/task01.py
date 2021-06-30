# min from 4 integers
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))
number4 = int(input("Enter number 4: "))
if number1 < number2 and number1 < number3 and number1 < number4:
    print("Minimum number is", number1)
elif number2 < number1 and number2 < number3 and number2 < number4:
    print("Minimum number is", number2)
elif number3 < number1 and number3 < number2 and number3 < number4:
    print("Minimum number is", number3)
else:
    print("Minimum number is", number4)