# 3. Person and Customer Classes
# Write a class named Person with data attributes for a person’s name, address, and telephone number. Next, write a class named Customer that is a subclass of the Person class.
# The Customer class should have a data attribute for a customer number, and a Boolean
# data attribute indicating whether the customer wishes to be on a mailing list. Demonstrate
# an instance of the Customer class in a simple program.

from customer import Customer


def main():
    name = input("Enter employee's name: ")
    address = input("Enter employee's address: ")
    phone_num = input(" Enter phone number: ")
    cust_num = int(input("Enter customer number: "))
    mail_list = int(input("Enter 11 if you want to be in a mailing list or 2 as no: "))
    customer = Customer(name, address, phone_num, cust_num, mail_list)
    print("Name: ", customer.get_name())
    print("Address: ", customer.get_address())
    print("Phone number: ", customer.get_phone_num())
    print("Customer number: ", customer.get_cust_num())
    print("Mailing list, UAH: ", customer.get_mail_list())


main()
