# 15. Kinetic Energy
# In physics, an object that is in motion is said to have kinetic energy. The following formula
# can be used to determine a moving object’s kinetic energy:
# KE 5 ½ mv2
# The variables in the formula are as follows: KE is the kinetic energy, m is the object’s mass
# in kilograms, and v is the object’s velocity in meters per second.
# Write a function named kinetic_energy that accepts an object’s mass (in kilograms)
# and velocity (in meters per second) as arguments. The function should return the amount
# of kinetic energy that the object has. Write a program that asks the user to enter values
# for mass and velocity, then calls the kinetic_energy function to get the object’s kinetic
# energy.


def main():
    mass = int(input("Enter the value for mass, kg: "))
    velocity = int(input("Enter value for velocity, m/s: "))
    ke = kineticEnergy(mass, velocity)
    print("The object’s kinetic energy: ", format(ke, '.2f'))


def kineticEnergy(mass, velocity):
    kinetEnergy = 1/2 * mass * (velocity ** 2)
    return kinetEnergy

main()
