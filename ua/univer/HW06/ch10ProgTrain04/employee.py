# # 4. Employee Class
# # Write a class named Employee that holds the following data about an employee in attributes:
# name, ID number, department, and job title.
# # Once you have written the class, write a program that creates three Employee objects to
# # hold the following data:
# # Name ID Number Department Job Title
# # Susan Meyers 47899 Accounting Vice President
# # Mark Jones 39119 IT Programmer
# # Joy Rogers 81774 Manufacturing Engineer
# # The program should store this data in the three objects, then display the data for each
# # employee on the screen.

class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def __str__(self):
        return f"Employee: name: {self.get_name()}," \
               f" id_number: {self.get_id_number()}," \
               f"department: {self.get_department()}, " \
               f"job title: {self.get_job_title()}"
