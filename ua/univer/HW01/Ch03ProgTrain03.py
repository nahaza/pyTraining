# Age classification
age = float(input('Enter the age of the person: '))
if 1 >= age >= 0:
    print("This person is an infant")
elif 1 < age < 13:
    print("This person is a child")
elif 13 <= age < 20:
    print("This person is a teenager")
elif age >= 20:
    print("This person is an adult")
