# # 3. Person and Customer Classes
# # Write a class named Person with data attributes for a person’s name, address, and telephone number. Next, write a class named Customer that is a subclass of the Person class.
# # The Customer class should have a data attribute for a customer number, and a Boolean
# # data attribute indicating whether the customer wishes to be on a mailing list. Demonstrate
# # an instance of the Customer class in a simple program.

class Person:
    def __init__(self, name, address, phone_num):
        self.__name = name
        self.__address = address
        self.__phone_num = phone_num

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_num(self, phone_num):
        self.__phone_num = phone_num

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_num(self):
        return self.__phone_num


class Customer(Person):
    def __init__(self, name, number, address, phone_num, cust_num, mail_list):
        Person.__init__(self, name, number, address, phone_num)
        self.__cust_num = cust_num
        self.__mail_list = mail_list

    def get_cust_num(self):
        return self.__cust_num

    def get_mail_list(self):
        if self.__mail_list ==1:
            return "Yes"
        else:
            return "No"
