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

import worker


def main():
    emp_name = input("Enter employee's name: ")
    emp_num = int(input("Enter employee's number: "))
    shift_num = int(input(" Enter 1 for day or 2 for night shift: "))
    pay_rate = float(input("Enter hour pay rate: "))
    employee = worker.ProductionWorker(emp_name, emp_num, shift_num, pay_rate)
    print("Name: ", employee.get_employee_name())
    print("Employee's number: ", employee.get_employee_number())
    print("Shift time: ", employee.get_shift_number())
    print("HHour pay rate: ", employee.get_pay_rate())


main()
