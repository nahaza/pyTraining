# 5. Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average rainfall over
# a period of years. The program should first ask for the number of years. The outer loop will
# iterate once for each year. The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
# After all iterations, the program should display the number of months, the total inches of
# rainfall, and the average rainfall per month for the entire period.

years = int(input("Enter the number of years: "))
month = 12
grandTotalRain = 0
for x in range(years):
    totalRain = 0
    print("\nYear #", x + 1)
    print("-------------------------------------")
    for y in range(month):
        print("Enter the amount of rainfall for month", y + 1, end='')
        rain = int(input(": "))
        totalRain += rain

    grandTotalRain += totalRain

numberOfMonth = years * month
avrRainfoll = grandTotalRain / numberOfMonth
print("The number of months:", numberOfMonth)
print("The total amount of rainfall, mm:", grandTotalRain)
print("The average rainfall for", numberOfMonth, "months", "per month, mm:", avrRainfoll)
