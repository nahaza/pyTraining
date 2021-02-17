# 5. Дано число месяца (тип int). Необходимо определить время года
# 	(зима, весна, лето, осень) и вывести на консоль.


def task05_print_season(month_number):
    if 1 <= month_number <= 12:
        if 1 <= month_number <= 2 or month_number == 12:
            season = 'Winter'
        elif 3 <= month_number <= 5:
            season = 'Spring'
        elif 6 <= month_number <= 8:
            season = 'Summer'
        else:
            season = 'Autumn'
        print(season)
    else:
        print("Enter the number of the month from 1 to 12. Reboot the program and try again")


month_number = int(input("Enter thr number of the month: "))
task05_print_season(month_number)
