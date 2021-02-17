# Mass and Weight
mass = float(input("Enter an object’s mass, kilograms: "))
weight = mass * 9.8
if weight > 500:
    print("The object’s mass is", format(weight, '.2f'), "newtons.", "It is too heavy.")
elif weight < 100:
    print("The object’s mass is", format(weight, '.2f'), "newtons.", "It is too light.")
else:
    print("The object’s mass is", format(weight, '.2f'), "newtons.")
