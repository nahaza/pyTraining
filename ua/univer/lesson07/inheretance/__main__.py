from ua.univer.lesson07.inheretance.humans import *


def print_name(human):
    print(human.name)

if __name__ == '__main__':
    stud1 = Student("Tom", 20, 11)
    doc1 = Doctor("Haus", 50, 6)
    fighter1 = Fighter("BruceLi", 30, 100, 75)

    human_list = [stud1, doc1, fighter1, Doctor("Aibolit", 60, 7)]
    for human in human_list:
        print(human)

    old_human = human_list[0]
    for human in human_list:
        if old_human.age < human.age:
            old_human = human
    print("old=", old_human)

    for human in human_list:
        if isinstance(human, Doctor):
            print("Licence:", human.name, human.id_licence)
        elif isinstance(human, Student):
            print("Group:", human.name, human.id_group)
    print_name(fighter1)

