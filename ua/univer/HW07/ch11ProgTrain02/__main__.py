# 2. ShiftSupervisor Class
# In a particular factory, a shift supervisor is a salaried employee who supervises a shift. In
# addition to a salary, the shift supervisor earns a yearly bonus when his or her shift meets
# production goals. Write a ShiftSupervisor class that is a subclass of the Employee class
# you created in Programming Exercise 1. The ShiftSupervisor class should keep a data
# attribute for the annual salary, and a data attribute for the annual production bonus that
# a shift supervisor has earned. Demonstrate the class by writing a program that uses a
# ShiftSupervisor object.

import supervisor


def main():
    name = input("Enter employee's name: ")
    number = int(input("Enter employee's number: "))
    salary = int(input(" Enter annual salary: "))
    pro_bonus = int(input("Enter production bonus: "))
    employee = supervisor.ShiftSupervisor(name, number, salary, pro_bonus)
    print("Name: ", employee.get_employee_name())
    print("Employee's number: ", employee.get_employee_number())
    print("Annual salary, UAH: ", employee.get_annual_salary())
    print("Production bonus, UAH: ", employee.get_annual_production_bonus())


main()
