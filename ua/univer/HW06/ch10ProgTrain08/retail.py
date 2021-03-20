# 8. Cash Register
# This exercise assumes you have created the RetailItem class for Programming Exercise 5. Create a CashRegister class that can be used with the RetailItem class. The
# CashRegister class should be able to internally keep a list of RetailItem objects. The
# class should have the following methods:
# • A method named purchase_item that accepts a RetailItem object as an argument.
# Each time the purchase_item method is called, the RetailItem object that is passed
# as an argument should be added to the list.
# • A method named get_total that returns the total price of all the RetailItem objects
# stored in the CashRegister object’s internal list.
# • A method named show_items that displays data about the RetailItem objects stored
# in the CashRegister object’s internal list.
# • A method named clear that should clear the CashRegister object’s internal list.
# Demonstrate the CashRegister class in a program that allows the user to select several
# items for purchase. When the user is ready to check out, the program should display a list
# of all the items he or she has selected for purchase, as well as the total price.


class RetailItem:
    def __init__(self, description, units, price):
        self.__description = description
        self.__units = units
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_units(self, units):
        self.__units = units

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"Description: " + self.__description + str(self.__units) + str(self.__price)
