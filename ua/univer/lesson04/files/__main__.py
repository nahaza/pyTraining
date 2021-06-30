if __name__ == '__main__':
    with open("text.txt", "a") as my_file:
        my_file.write(("\nhi people"))

    with open("text.txt", "r") as my_file:
        for line in my_file:
            print(line, end='')

