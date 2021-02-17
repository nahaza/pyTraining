# Planting Grapevines
R = float(input("Enter the length of the row, m: "))
E = float(input("Enter the amount of space used by an end-post assembly, m: "))
S = float(input("Enter the space between vines, m: "))
numberOfGrapevinesInRow = (R - 2 * E) // S
print("The number of grapevines in a row is", format(numberOfGrapevinesInRow, '.0f'), "items")
