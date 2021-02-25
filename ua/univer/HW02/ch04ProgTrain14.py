# 14. Write a program that uses nested loops to draw this pattern:
# *******
# ******
# *****
# ****
# ***
# **
# *

for x in range(7, 0, -1):
    for y in range(x, 0, -1):
        print("*", end='')
    print()
