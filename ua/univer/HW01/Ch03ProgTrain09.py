# Roulette Wheel Colors
pocketNumber = int(input("Enter a pocket number from 0 to 36: "))
colour1 = 'green'
colour2 = 'red'
colour3 = 'black'
if 0 <= pocketNumber <= 36:
    if pocketNumber == 0:
        colour = colour1
    elif 1 <= pocketNumber <= 10:
        if pocketNumber % 2 > 0:
            colour = colour2
        else:
            colour = colour3
    elif 11 <= pocketNumber <= 18:
        if pocketNumber % 2 > 0:
            colour = colour3
        else:
            colour = colour2
    elif 19 <= pocketNumber <= 28:
        if pocketNumber % 2 > 0:
            colour = colour2
        else:
            colour = colour3
    elif 29 <= pocketNumber <= 36:
        if pocketNumber % 2 > 0:
            colour = colour3
        else:
            colour = colour2
    print("The pocket number colour is", colour)
else:
    print("Warning, pocket number should be from 0 to 36")

