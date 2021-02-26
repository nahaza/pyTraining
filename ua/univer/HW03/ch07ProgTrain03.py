# 3. Rainfall Statistics
# Design a program that lets the user enter the total rainfall for each of 12 months into a
# list. The program should calculate and display the total rainfall for the year, the average
# monthly rainfall, the months with the highest and lowest amounts.

def main():
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    amount = []
    total = 0

    print("Enter rainfall for each month: ")
    for rainfall in month:
        rainfall = float(input(rainfall + ': '))
        amount.append(rainfall)
    for rainfall in amount:
        total += rainfall
    print("Total rainfall for the year:", total)
    print("The average monthly rainfall:", format(total / 12, '.1f'))

    monthMax = max(amount)
    monthMaxIndex = amount.index(monthMax)
    monthMaxMonth = month[monthMaxIndex]

    monthMin = min(amount)
    monthMinIndex = amount.index(monthMin)
    monthMinMonth = month[monthMinIndex]

    print("The months with the highest amounts:", monthMaxMonth)
    print("The months with the lowest amounts:", monthMinMonth)


main()
