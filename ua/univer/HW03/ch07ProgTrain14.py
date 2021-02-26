# 14. Expense Pie Chart
# Create a text file that contains your expenses for last month in the following categories:
# •	 Rent
# •	 Gas
# •	 Food
# •	 Clothing
# •	 Car payment
# •	 Misc
# Write a Python program that reads the data from the file and uses matplotlib to plot a pie
# chart showing how you spend your money.

import matplotlib.pyplot as plt


def getData(file):
    expensList = []
    dataFromFile = open(file, 'r')
    for x in dataFromFile:
        x = x.rstrip('\n')
        expensList.append(x)
    return expensList


def getExpensLabel():
    expensLabel = ['Rent', 'Gas', 'Food', 'Clothing', 'Car payment', 'Misc']
    return expensLabel


def main():
    expensList = getData('expenses.txt')
    expensLabel = getExpensLabel()
    plt.pie(expensList, labels=expensLabel)
    plt.title("Expense Pie Chart")
    plt.show()


main()
