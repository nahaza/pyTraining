# 7. Employee Management System
# This exercise assumes you have created the Employee class for Programming Exercise 4.
# Create a program that stores Employee objects in a dictionary. Use the employee ID number as the key. The program should present a menu that lets the user perform the following
# actions:
# • Look up an employee in the dictionary
# • Add a new employee to the dictionary
# • Change an existing employee’s name, department, and job title in the dictionary
# • Delete an employee from the dictionary
# • Quit the program
# When the program ends, it should pickle the dictionary and save it to a file. Each time the
# program starts, it should try to load the pickled dictionary from the file. If the file does not
# exist, the program should start with an empty dictionary.

import pickle
import employee

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
FILENAME = 'employees.dat'


def main():
    employees = load_employees()
    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(employees)
        elif choice == ADD:
            add(employees)
        elif choice == CHANGE:
            change(employees)
        elif choice ++ DELETE:
            delete(employees)
    save_employees(employees)


def load_employees():
    try:
        input_file = open(FILENAME, 'rb')
        employee_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        employee_dct = {}
    return employee_dct


def get_menu_choice():
    print()
    print("Menu")
    print("------------------------------------------------------")
    print("1. Look up an employee")
    print("2. Add a new employee")
    print("3. Change employee paratameters")
    print("4. Delete an employee")
    print("5. Quit the program")
    print()
    choice = int(input("Enter your choice"))
    while choice < LOOK_UP or choice> QUIT:
        choice = int(input("Enter a valid choice: "))
    return choice


def look_up(employees):
    id = int(input("Enter ID number: "))
    print()
    print(employees.get(id, "Thar ID is not found"))


def add(employees):
    id = int(input("Enter ID number: "))
    name = input("Enter a name: ")
    dep = input("Enter the department: ")
    job = input("Enter the job title: ")
    entry = employee.Employee(id, name, dep, job)
    if id not in employees:
        employees[id] = entry
        print("Added")
    else:
        print("That ig already exists")


def change(employees):
    id = int(input("Enter ID number: "))
    if id in employees:
        name = input("Enter a name: ")
        dep = input("Enter the department: ")
        job = input("Enter the job title: ")
        entry = employee.Employee(id, name, dep, job)
        employees[id] = entry
        print("Updated")
    else:
        print("ID not found")


def delete(employees):
    id = int(input("Enter ID number: "))
    if id in employees:
        del employees[id]
        print("Deleted")
    else:
        print("ID not found")


def save_employees(employees):
    output_file = open(FILENAME, 'wb')
    pickle.dump(employees, output_file)
    output_file.close()


main()
