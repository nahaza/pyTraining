# TO STUDY LATER!!!!!!!!!
# 14. Gas Prices
# In the student sample program files for this chapter, you will find a text file named
# GasPrices.txt. The file contains the weekly average prices for a gallon of gas in the
# United States, beginning on April 5th, 1993, and ending on August 26th, 2013. Figure 8-7
# shows an example of the first few lines of the file’s contents:
# Each line in the file contains the average price for a gallon of gas on a specific date. Each line
# is formatted in the following way:
#  MM-DD-YYYY:Price
# MM is the two-digit month, DD is the two-digit day, and YYYY is the four-digit year. Price is
# the average price per gallon of gas on the specified date.
# For this assignment, you are to write one or more programs that read the contents of the file
# and perform the following calculations:
# Average Price Per Year: Calculate the average price of gas per year, for each year in the file.
# (The file’s data starts in April of 1993, and it ends in August 2013. Use the data that is present for the years 1993 and 2013.)
# Average Price Per Month: Calculate the average price for each month in the file.
# Highest and Lowest Prices Per Year: For each year in the file, determine the date and amount
# for the lowest price, and the highest price.
# List of Prices, Lowest to Highest: Generate a text file that lists the dates and prices, sorted
# from the lowest price to the highest.
# List of Prices, Highest to lowest: Generate a text file that lists the dates and prices, sorted
# from the highest price to the lowest.
# You can write one program to perform all of these calculations, or you can write different
# programs, one for each calculation.

from datetime import datetime as dt


def yearWiseAveragePrices(priceList):
    year = 1993
    initSum = 0
    count = 0
    for date, price in priceList:
        dateYear = date.year
        if dateYear != year:
            print('{}:{:.3f}'.format(year, initSum/count))
            year = dateYear
            count = 0
            initSum = 0
        initSum += price
        count += 1


def monthWiseAveragePrices(priceList):
    monthNameList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    year = 1993
    month = 4
    initSum = 0
    count = 0
    for date, price in priceList:
        dateYear = date.year
        dateMonth = date.month
        if dateMonth != month:
            print('{}, {}: {:.3f}'.format(monthNameList[month-1], year, initSum/count))
            year = dateYear
            month = dateMonth
            count = 0
            initSum = 0
        initSum += price
        count += 1


def getFileLowToHigh(priceList):
    newSortedList = sorted(priceList, key=lambda x:x[1])
    f = open('lowToHigh.txt', 'x')
    for date, price in newSortedList:
        f.write('{}: {}\n'.format(date.strftime('%m-%d-%Y'), price))
    f.close()


def getFileHighToLow(priceList):
    newSortedList = sorted(priceList, key=lambda x:x[1], reverse=True)
    f = open('highToLow.txt', 'x')
    for date, price in newSortedList:
        f.write('{}: {}\n'.format(date.strftime('%m-%d-%Y'), price))
    f.close()


def main():
    f = open('gasPrices.txt', 'r')
    priceList = []
    for line in f:
        line = line.split(':')
        dateObj = dt.strftime(line[0], '%m-%d-%Y')
        avgPrice = float(line[1])
        priceList.append((dateObj, avgPrice))
        priceList.append((dt.today(), -1))
        yearWiseAveragePrices(priceList)
        monthWiseAveragePrices(priceList)
        priceList.pop()
        getFileLowToHigh(priceList)
        getFileHighToLow(priceList)


if __name__ == '__main__':
    main()