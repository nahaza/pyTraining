# 3. Date Printer
# Write a program that reads a string from the user containing a date in the form mm/dd/yyyy.
# It should print the date in the format March 12, 2018.

def getDate(inputDate):
    dateList = inputDate.split('/')
    month = int(dateList[0])
    day = dateList[1]
    year = dateList[2]
    return month, day, year


def printDate(month, day, year):
    nameMonth = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December']
    monthToPrint = nameMonth[month-1]
    dateToPrint = (monthToPrint+' '+day+", "+year)
    return dateToPrint


def main():
    inputDate = input("Enter a date in the form mm/dd/yyyy: ")
    month, day, year = getDate(inputDate)
    dateToPrint = printDate(month, day, year)
    print(dateToPrint)


main()

