# 14. Falling Distance
# When an object is falling because of gravity, the following formula can be used to determine
# the distance the object falls in a specific time period:
# d 5 ½ gt2
# The variables in the formula are as follows: d is the distance in meters, g is 9.8, and t is the
# amount of time, in seconds, that the object has been falling.
# Write a function named falling_distance that accepts an object’s falling time (in seconds)
# as an argument. The function should return the distance, in meters, that the object has
# fallen during that time interval. Write a program that calls the function in a loop that passes
# the values 1 through 10 as arguments and displays the return value.


g = 9.8
minArgument = 1
maxArgument = 10


def main():
    print("Time\tFalling distance, m")
    print("----\t-------------------")
    for fallingTime in range(minArgument, maxArgument + 1):
        fallDistance = fallingDistance(fallingTime)
        print(fallingTime, '\t\t\t', format(fallDistance, '.1f'))


def fallingDistance(fallingTime):
    return 1 / 2 * g * (fallingTime ** 2)


main()
