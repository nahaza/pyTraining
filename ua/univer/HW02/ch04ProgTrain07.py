# 7. Pennies for Pay
# Write a program that calculates the amount of money a person would earn over a period of
# time if his or her salary is one penny the first day, two pennies the second day, and continues
# to double each day. The program should ask the user for the number of days. Display
# a table showing what the salary was for each day, then show the total pay at the end of the
# period. The output should be displayed in a dollar amount, not the number of pennies.

days = int(input("Enter the number of days to assess the salary: "))
totalSalary = 0
salaryStart = 0.01
print("Days", "\t\t\t", "Salary, UAH")
for i in range(days):
    salary = salaryStart * (2 ** i)
    print(i+1, "\t\t\t\t", format(salary, '.2f'))
    totalSalary += salary

print("--------------------------------")
print("Overall:")
print("--------------------------------")
print(days, "\t\t\t\t", format(totalSalary, '.2f'))

