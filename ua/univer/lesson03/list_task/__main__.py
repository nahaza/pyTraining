import tasks_list

if __name__ == '__main__':
    list_even = None
    list_odd = None
    while True:
        print("""1.создайте массив, содержащий 10 первых нечетных чисел.
            Выведете элементы массива на консоль в одну строку, разделяя запятой""")
        print("""2.ввести 10 целых значений с консоли и разместить в 2 масива четные и нечетные""")
        print("""3.подсчитать сколько четные и нечетные""")
        print("""4.сумма елементов в каждом масиве и среднее арифметическое""")
        print("""6.Дан массив размерности N,  найти наименьший элемент массива""")
        print("""7.Поменять наибольший и наименьший элементы массива местами""")
        print("0. Exit")

        answer = input("Enter choice: ")
        if answer == "0":
            break
        elif answer == "1":
            print(tasks_list.task01_get10odd())
        elif answer == "2":
            list_even, list_odd = tasks_list.get_even_odd_list_from_console()
            print(list_even)
            print(list_odd)
        elif answer == "3":
            if list_even == None or list_odd == None:
                print("list_even == None or list_odd == None")
                print("try choice task 2 first")
                continue
            print("len list_even=", len(list_even))
            print("len list_odd=", len(list_odd))
        elif answer == "4":
            if list_even == None or list_odd == None:
                print("list_even == None or list_odd == None")
                print("try choice task 2 first")
            else:
                print("sum even =", tasks_list.get_sum(list_even))
                print("sum odd =", tasks_list.get_sum(list_odd))
                print("average even =", tasks_list.get_average(list_even))
                print("average odd =", tasks_list.get_average(list_odd))
        elif answer == "6":
            if list_even == None or list_odd == None:
                print("list_even == None or list_odd == None")
                print("try choice task 2 first")
            else:
                print("min even =", min(list_even))
                print("min odd =", min(list_odd))
                print("count min even =", list_even.count((min(list_even))))
                print("count min odd =", list_odd.count(min(list_odd)))
        elif answer == "7":
            if list_even == None or list_odd == None:
                print("list_even == None or list_odd == None")
                print("try choice task 2 first")
            else:
                tasks_list.change_v2_man_max_in_list(list_even)
                tasks_list.change_v2_man_max_in_list(list_odd)
        else:
            print("Error in choice")
