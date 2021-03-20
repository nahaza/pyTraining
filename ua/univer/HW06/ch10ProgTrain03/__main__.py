# # 3. Personal Information Class
# # Design a class that holds the following personal data: name, address, age, and phone number. Write appropriate accessor and mutator methods. Also, write a program that creates
# # three instances of the class. One instance should hold your information, and the other two
# # should hold your friends’ or family members’ information.

import info


def main():
    address_book = []
    for _ in range(3):
        print("Enter info about 3 people")
        name = input("Enter name: ")
        address = input("Enter address: ")
        age = int(input("Enter age: "))
        phone_num = int(input("Enter phone_number: "))
        person = info.Person(name, address, age, phone_num)
        address_book.append(person)

    for _ in address_book:
        print(person)

main()
