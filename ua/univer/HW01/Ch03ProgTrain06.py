# Magic Dates
month = int(input("Enter a month in numeric form: "))
day = int(input("Enter a day in numeric form: "))
year = int(input("Enter a two-digit year: "))
monthTimesDay = month * day
if monthTimesDay == year:
    print("The date is magic")
else:
    print("The date is not magic")
