# 1. Employee and ProductionWorker Classes
# Write an Employee class that keeps data attributes for the following pieces of information:
# •	 Employee name
# •	 Employee number
# Next, write a class named ProductionWorker that is a subclass of the Employee class.
# The ProductionWorker class should keep data attributes for the following information:
# •	 Shift number (an integer, such as 1, 2, or 3)
# •	 Hourly pay rate
# The workday is divided into two shifts: day and night. The shift attribute will hold an
# integer value representing the shift that the employee works. The day shift is shift 1 and the
# night shift is shift 2. Write the appropriate accessor and mutator methods for each class.
# Once you have written the classes, write a program that creates an object of the
# ProductionWorker class and prompts the user to enter data for each of the object’s data
# attributes. Store the data in the object, then use the object’s accessor methods to retrieve it
# and display it on the screen.

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


class ProductionWorker(Employee):
    def __init__(self,emp_name, emp_num, sift_num, pay_rate):
        Employee.__init__(self, emp_name, emp_num)
        self.__shift_number = sift_num
        self.__pay_rate = pay_rate

    def set_shift_number(self, shift_num):
        self.__shift_number = shift_num

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def get_shift_number(self):
        if self.__shift_number ==1:
            return "Day"
        if self.__shift_number ==2:
            return "Night"

    def get_pay_rate(self):
        return self.__pay_rate
