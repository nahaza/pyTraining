# 2. Calories Burned
# Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
# uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

caloriesBurnMinute = 4.2
for i in range(10, 31, 5):
    totalBurned = caloriesBurnMinute * i
    print("You burned " + str(totalBurned) + ' calories for ' + str(i) + ' minutes')
