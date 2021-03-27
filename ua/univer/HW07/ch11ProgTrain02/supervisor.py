 # 2. ShiftSupervisor Class
# In a particular factory, a shift supervisor is a salaried employee who supervises a shift. In
# addition to a salary, the shift supervisor earns a yearly bonus when his or her shift meets
# production goals. Write a ShiftSupervisor class that is a subclass of the Employee class
# you created in Programming Exercise 1. The ShiftSupervisor class should keep a data
# attribute for the annual salary, and a data attribute for the annual production bonus that
# a shift supervisor has earned. Demonstrate the class by writing a program that uses a
# ShiftSupervisor object.

class Employee:
    def __init__(self, emp_name, emp_num):
        self.__employee_name = emp_name
        self.__employee_number = emp_num

    def set_employee_name(self, emp_name):
        self.__employee_name = emp_name

    def set_employee_number(self, emp_num):
        self.__employee_number = emp_num

    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number


class ShiftSupervisor(Employee):
    def __init__(self,name, num, salary, production_bonus):
        super().__init__(name, num)
        self.__annual_salary = salary
        self.__annual_production_bonus = production_bonus

    def set_annual_salary(self, salary):
        self.__annual_salary = salary


    def set_annual_production_bonus(self, production_bonus):
        self.__annual_production_bonus = production_bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def get_annual_production_bonus(self):
        return self.__annual_production_bonus
