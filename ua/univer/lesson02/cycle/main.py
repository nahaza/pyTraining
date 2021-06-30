import tasks_cycle

while True:
    print("-------------MENU--------------")
    print("1.pritn_10_positive")
    print("2.power")
    print("0.Exit")
    print("----make a choice----------")
    answer = int(input("Enter choice: "))
    if answer == 0:
        break;
    elif answer == 1:
        tasks_cycle.calc_power_from_console()
    elif answer == 2:
        print(tasks_cycle.power(3,2))
    else:
        print("wrong choice")

