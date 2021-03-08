# 10. Most Frequent Character
# Write a program that lets the user enter a string and displays the character that appears most
# frequently in the string.

def main():
    letterFrequency = [0] * 256
    myString = input("Enter your string: ")
    for letter in myString:
        letterFrequency[ord(letter)] += 1
    print(chr(letterFrequency.index(max(letterFrequency))))


if __name__ == '__main__':
    main()
