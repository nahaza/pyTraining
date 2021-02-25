# 15. Write a program that uses nested loops to draw this pattern:
# ##
# # #
# # #
# # #
# # #
# # #


for x in range(6):
    print("#", end='')
    for y in range(x):
        print(" ", end='')
    print('#')
