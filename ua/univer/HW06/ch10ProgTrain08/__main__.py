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

from retail import RetailItem
from cash_register import CashRegister

def main():
    register = CashRegister()
    descr_list = ["Jacket", "Designer Jeans", "Shirt"]
    unit_list = [12, 40, 20]
    price_list = [59.95, 34.95, 24.95]
    for i in range(3):
        descr = descr_list[i]
        units = unit_list[i]
        price = price_list[i]
        item = RetailItem(descr, units, price)
        register.purchase_item(item)

        print("Cash Register")
        print("_____________________________________")
        register.show_items()


main()
