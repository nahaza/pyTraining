# Body Mass Index
weight = float(input("Enter your weight, kg: "))
height = float(input("Enter your height, m: "))
bmi = weight / height
if weight <= 0 or height <= 0:
    print("Enter valid weight and height")
else:
    if 18.5 <= bmi <= 25:
        print("Your weight is optimal, BMI is", format(bmi, '.1f'))
    elif bmi < 18.5:
        print("You are underweight, BMI is", format(bmi, '.1f'))
    else:
        print("You are overweight, BMI is", format(bmi, '.1f'))
