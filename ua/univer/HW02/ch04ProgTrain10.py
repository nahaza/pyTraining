# 10. Tuition Increase
# At one college, the tuition for a full-time student is $8,000 per semester. It has been announced
# that the tuition will increase by 3 percent each year for the next 5 years. Write a program
# with a loop that displays the projected semester tuition amount for the next 5 years.

tuition = 8000.00
yearStart = 2022
numberOfYears = 5
rise = 0.03
print('------------------------------')
print('Year            Tuition, UAH')
print('------------------------------')
for i in range(yearStart, yearStart + numberOfYears):
    tuition += rise * tuition
    print(i, "\t\t\t", format(tuition, '.2f'))

