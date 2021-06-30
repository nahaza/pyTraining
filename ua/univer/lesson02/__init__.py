def task05_print_season(month_number):
    if month_number == 1 or month_number == 2 or month_number == 12:
        season = 'Winter'
    elif month_number == 3 or month_number == 4 or month_number == 5:
        season = 'Spring'
    elif month_number == 6 or month_number == 7 or month_number == 8:
        season = 'Summer'
    elif month_number == 9 or month_number == 10 or month_number == 11:
        season = 'Autumn'
    print(season)


month_number = input("Enter month_number: ")
task05_print_season()
