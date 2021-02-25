# 6. Calories from Fat and Carbohydrates
# A nutritionist who works for a fitness club helps members by evaluating their diets. As part
# of her evaluation, she asks members for the number of fat grams and carbohydrate grams
# that they consumed in a day. Then, she calculates the number of calories that result from
# the fat, using the following formula:
# calories from fat 5 fat grams 3 9
# Next, she calculates the number of calories that result from the carbohydrates, using the
# following formula:
# calories from carbs 5 carb grams 3 4
# The nutritionist asks you to write a program that will make these calculations.

fatToCalories = 9
carbsToCalories = 4


def getCaloriesFromFat(fat):
    getCaloriesFromFat = fat * fatToCalories
    return getCaloriesFromFat


def getCaloriesFromCarbs(carbs):
    getCaloriesFromCarbs = carbs * carbsToCalories
    return getCaloriesFromCarbs


def main():
    fat = int(input("Enter the number of fat grams consumed in a day: "))
    carbs = int(input("Enter the number of carbohydrate grams consumed in a day: "))
    print("The number of calories that result from the fat =", getCaloriesFromFat(fat))
    print("The number of calories that result from the carbohydrates =", getCaloriesFromCarbs(carbs))


main()
