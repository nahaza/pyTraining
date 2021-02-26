# 4. Number Analysis Program
# Design a program that asks the user to enter a series of 20 numbers. The program should
# store the numbers in a list then display the following data:
# •	 The lowest number in the list
# •	 The highest number in the list
# •	 The total of the numbers in the list
# •	 The average of the numbers in the list

def main():
    numbers = []
    total = 0

    for num in range(1, 21):
        num = int(input("Enter the number " + str(num) + ": "))
        numbers.append(num)
        total += num
        average = total / len(numbers)
    print("The lowest number in the list", min(numbers))
    print("The highest number in the list", max(numbers))
    print("The total of the numbers in the list:", total)
    print("The average of the numbers in the list", average)


main()
