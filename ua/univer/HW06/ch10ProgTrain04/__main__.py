# 4. Employee Class
# Write a class named Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.
# Once you have written the class, write a program that creates three Employee objects to
# hold the following data:
# Name ID Number Department Job Title
# Susan Meyers 47899 Accounting Vice President
# Mark Jones 39119 IT Programmer
# Joy Rogers 81774 Manufacturing Engineer
# The program should store this data in the three objects, then display the data for each
# employee on the screen.

import employee


def main():
    employees = []
    employee1 = employee.Employee('Susan Meyers','47899','Accounting','Vice President')
    employee2 = employee.Employee('Mark Jones', '39119','IT','Programmer')
    employee3 = employee.Employee('Joy Rogers', '81774','Manufacturing','Engineer')
    employees = [employee1, employee2, employee3]
    print('-------------------------------------------------------------------------------------')
    print('                           Employees                                                 ')
    print('-------------------------------------------------------------------------------------')
    for x in employees:
        print(x)
    print('-------------------------------------------------------------------------------------')


main()
