# colour mixer
colour1 = str.lower(input("Enter the first colour: "))
colour2 = str.lower(input("Enter the second colour: "))
if colour1 == 'red' and colour2 == 'blue':
    print("You get purple")
elif colour2 == 'red' and colour1 == 'blue':
    print("You get purple")
elif colour1 == 'red' and colour2 == 'yellow':
    print("You get orange")
elif colour2 == 'red' and colour1 == 'yellow':
    print("You get orange")
elif colour1 == 'blue' and colour2 == 'yellow':
    print("You get green")
elif colour2 == 'blue' and colour1 == 'yellow':
    print("You get green")
elif colour1 != 'red' and colour1 != 'blue' and colour1 != 'yellow':
    print("Warning: enter the first colour from red, blue, yellow")
    if colour2 != 'red' and colour2 != 'blue' and colour2 != 'yellow':
        print("Warning: enter the second colour from red, blue, yellow")


# alternative answer
colour1 = str.lower(input("Enter the first colour: "))
colour2 = str.lower(input("Enter the second colour: "))
mix = colour1 + colour2
if mix == 'redblue' or mix == 'bluered':
    print("You get purple")
elif mix == 'redyellow' or mix == 'yellowred':
    print("You get orange")
elif mix == 'blueyellow' or mix == 'yellowblue':
    print("You get green")
elif mix == 'redred' or mix == 'blueblue' or mix == 'yellowyellow':
    print("Your colour remains the same:", colour1)
elif colour1 != 'red' and colour1 != 'blue' and colour1 != 'yellow':
    print("Warning: enter the first colour from red, blue, yellow")
    if colour2 != 'red' and colour2 != 'blue' and colour2 != 'yellow':
        print("Warning: enter the second colour from red, blue, yellow")

# alternative answer
colour1 = str.lower(input("Enter the first colour: "))
colour2 = str.lower(input("Enter the second colour: "))
mix = colour1 + colour2
if colour1 != colour2:
    if mix == 'redblue' or mix == 'bluered':
        print("You get purple")
    elif mix == 'redyellow' or mix == 'yellowred':
        print("You get orange")
    elif mix == 'blueyellow' or mix == 'yellowblue':
        print("You get green")
    elif colour1 != 'red' and colour1 != 'blue' and colour1 != 'yellow':
        print("Warning: enter the first colour from red, blue, yellow")
        if colour2 != 'red' and colour2 != 'blue' and colour2 != 'yellow':
            print("Warning: enter the second colour from red, blue, yellow")
else:
    print("Your colour remains the same:", colour1)
