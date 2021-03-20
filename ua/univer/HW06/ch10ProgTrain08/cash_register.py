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

class CashRegister:
    def __init__(self, item_list = []):
        self.item_list = item_list
        self.list_sum = 0

    def purchase_item(self, ri_obj):
        self.item_list.append(ri_obj)
        self.list_sum += ri_obj.get_price()

    def get_total(self):
        return self.list_sum

    def show_items(self):
        for item in range(len(self.item_list)):
            print((self.item_list[item]))
            print("---------------------------------------")

    def clear(self):
        self.item_list.clear()
