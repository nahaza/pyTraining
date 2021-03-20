hour = int(input("Enter time hour: "))
age = int(input("Enter age: "))
if hour < 22:
    if age > 18:
        print("You can buy alcohol")
    else:
        print("You can buy pepsi")
else:
    print("market is closed")
