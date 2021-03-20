# 3. Personal Information Class
# Design a class that holds the following personal data: name, address, age, and phone number. Write appropriate accessor and mutator methods. Also, write a program that creates
# three instances of the class. One instance should hold your information, and the other two
# should hold your friends’ or family members’ information.

class Person:
    def __init__(self, name, address, age, phone_num):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_num = phone_num

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_num(self, phone_num):
        self.__phone_num = phone_num

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_num(self):
        return self.__phone_num

    def __str__(self):
        return f"Person: name: {self.get_name()}," \
               f" address: {self.get_address()}," \
               f"age: {self.get_age()}, " \
               f"phone number: {self.get_phone_num()}"
