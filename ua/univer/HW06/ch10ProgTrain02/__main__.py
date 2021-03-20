# 2. Car Class
# Write a class named Car that has the following data attributes:
# • _ _year_model (for the car’s year model)
# • _ _make (for the make of the car)
# • _ _speed (for the car’s current speed)
# The Car class should have an _ _init_ _ method that accepts the car’s year model and
# make as arguments. These values should be assigned to the object’s _ _year_model and
# _ _make data attributes. It should also assign 0 to the _ _speed data attribute.
# The class should also have the following methods:
# • accelerate
# The accelerate method should add 5 to the speed data attribute each time it is called.
# • brake
# The brake method should subtract 5 from the speed data attribute each time it is called.
# • get_speed
# The get_speed method should return the current speed.
# Next, design a program that creates a Car object then calls the accelerate method five
# times. After each call to the accelerate method, get the current speed of the car
# and display it. Then call the brake method five times. After each call to the brake method, get the
# current speed of the car and display it.

import car


def main():
    my_car = car.Car(2019, 'Land Rover', 50)
    for _ in range(5):
        print("Accelerating the car")
        my_car.accelerate()
        print("Current speed: ", my_car.get_speed())
    for _ in range(5):
        print("Applying the breaks")
        my_car.brake()
        print("Current speed: ", my_car.get_speed())


main()
