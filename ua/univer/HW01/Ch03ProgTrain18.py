# Restaurant Selector
vegetarian = str.lower(input("Is anyone in your party a vegetarian? Yes or No: "))
vegan = str.lower(input("Is anyone in your party a  vegan? Yes or No: "))
glutenfree = str.lower(input("Is anyone in your party a gluten-free? Yes or No: "))
if vegetarian == 'yes':
    if vegan == 'yes':
        if glutenfree == 'yes':
            print("Corner Café—Vegetarian \nThe Chef’s Kitchen")
        elif glutenfree == 'no':
            print("Corner Café—Vegetarian \nThe Chef’s Kitchen")
        else:
            print("Enter Yes or No. Rerun the program")
    elif vegan == 'no':
        if glutenfree == 'yes':
            print("Main Street Pizza Company \nCorner Café—Vegetarian \nThe Chef’s Kitchen")
        elif glutenfree == 'no':
            print("Main Street Pizza Company \nCorner Café—Vegetarian \n"
                  "Mama’s Fine Italian \nThe Chef’s Kitchen")
        else:
            print("Enter Yes or No. Rerun the program")
elif vegetarian == 'no':
    if vegan == 'yes':
        if glutenfree == 'yes':
            print("Corner Café—Vegetarian \nThe Chef’s Kitchen")
        elif glutenfree == 'no':
            print("Corner Café—Vegetarian \nThe Chef’s Kitchen")
        else:
            print("Enter Yes or No. Rerun the program")
    elif vegan == 'no':
        if glutenfree == 'yes':
            print("Main Street Pizza Company \nCorner Café—Vegetarian \nThe Chef’s Kitchen")
        elif glutenfree == 'no':
            print("Joe’s Gourmet Burgers\nMain Street Pizza Company\nCorner Café—Vegetarian\n"
                  "Mama’s Fine Italian\nThe Chef’s Kitchen")
        else:
            print("Enter Yes or No. Rerun the program")
    else:
        print("Enter Yes or No. Rerun the program")
else:
    print("Enter Yes or No. Rerun the program")
