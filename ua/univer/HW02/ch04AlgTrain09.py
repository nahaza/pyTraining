# Напишите программный код, который предлагает пользователю ввести число в диапазоне
# от 1 до 100 и проверяет допустимость введенного значения.

num = int(input("Enter a positive nonzero number  from 1 to 100: "))
while num <= 0 or num >= 100:
    print("Warning: it is not a positive nonzero number from 1 to 100")
    num = int(input("Enter a positive nonzero number from 1 to 100: "))
