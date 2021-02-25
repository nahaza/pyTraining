# 3. Анализ бюджета. Напишите программу, которая просит пользователя ввести сумму,
# выделенную им на один месяц. Затем цикл должен предложить пользователю ввести
# суммы отдельных статей его расходов за месяц и подсчитать их нарастающим итогом. По
# завершению цикла программа должна вывести сэкономленную или перерасходованную
# сумму.

keepOn = 'y'
budget = float(input("Enter your month budget: "))
totalExpens = 0
while keepOn == 'y' or keepOn == 'Y':
    expenses = float(input("Enter your expenses, UAH: "))
    totalExpens += expenses
    keepOn = str(input("Do you want to enter more expenses? Enter Y for yes: "))
budgetLeft = budget - totalExpens
if budgetLeft > 0:
    print("You have", budgetLeft, "UAH left")
elif budgetLeft == 0:
    print("You have no money left")
else:
    print("You are over your budget by", budgetLeft, "UAH")



