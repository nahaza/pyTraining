# Wi-Fi Diagnostic Tree
print("Reboot the computer and try to connect")
answer = str.lower(input("Did that fix the problem? Yes or No: "))
if answer == 'no':
    print("Reboot the router and try to connect.")
    answer = str.lower(input("Did that fix the problem? Yes or No: "))
    if answer == 'no':
        print("Make sure the cables between the router & modem are plugged in firmly")
        answer = str.lower(input("Did that fix the problem? Yes or No: "))
        if answer == 'no':
            print("Move the router to a new location and try to connect")
            answer = str.lower(input("Did that fix the problem? Yes or No: "))
            if answer == 'no':
                print("Get a new router")
            elif answer == 'yes':
                print("Congratulations")
            else:
                print("Enter Yes or No. Rerun the program")
        elif answer == 'yes':
            print("Congratulations")
        else:
            print("Enter Yes or No. Rerun the program")
    elif answer == 'yes':
        print("Congratulations")
    else:
        print("Enter Yes or No. Rerun the program")
elif answer == 'yes':
    print("Congratulations")
else:
    print("Enter Yes or No. Rerun the program")
