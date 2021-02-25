# The distance a vehicle travels can be calculated as follows:
# distance 5 speed 3 time
# For example, if a train travels 40 miles per hour for three hours, the distance traveled is
# 120 miles. Write a program that asks the user for the speed of a vehicle (in miles per hour)
# and the number of hours it has traveled. It should then use a loop to display the distance
# the vehicle has traveled for each hour of that time period

speed = int(input("Enter the speed of a vehicle, km/h: "))
hours = int(input("Enter the number of hours traveled, h: "))
distance = speed * hours
print('------------------------------')
print('Hour        Distance Traveled')
print('------------------------------')
for i in range(hours):
    print(i+1, '             ', distance)
