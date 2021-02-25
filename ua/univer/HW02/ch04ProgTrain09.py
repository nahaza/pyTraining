# 9. Ocean Levels
# Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an
# application that displays the number of millimeters that the ocean will have risen each year
# for the next 25 years.

risePerYear = 1.6
yearStart = 2022
numberOfYears = 25
rise = 0
print('------------------------------')
print('Year              Rise, mm')
print('------------------------------')
for year in range(yearStart, yearStart+numberOfYears):
    rise += risePerYear
    print(year, "\t\t\t\t", format(rise, '.1f'))

