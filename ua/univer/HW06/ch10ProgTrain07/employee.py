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

class Employee:
    def __init__(self, id, name, dep, job):
        self.__name = name
        self.__id = id
        self.__dep = dep
        self.__job = job

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_dep(self, dep):
        self.__dep = dep

    def set_job(self, job):
        self.__job = job

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dep(self):
        return self.__dep

    def get_job(self):
        return self.__job

    def __str__(self):
        return f"ID Number: {self.get_id()}," \
                f"Name: {self.get_name()}," \
               f"department: {self.get_dep()}, " \
               f"job title: {self.get_job()}"
