# Book Club Points
numberOfBooks = int(input("Enter the number of books that he or she has purchased this month: "))
level0 = 0
level1 = 2
level2 = 4
level3 = 6
level4 = 7
if numberOfBooks < level0:
    print("Warning, enter the valid number of books.")
else:
    if level0 <= numberOfBooks < level1:
        points = 0
    elif level1 <= numberOfBooks < level2:
        points = 5
    elif level2 <= numberOfBooks < level3:
        points = 15
    elif level3 <= numberOfBooks <= level4:
        points = 30
    else:
        points = 60
    print("You get", points, "points")
