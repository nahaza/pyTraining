# 9. Vowels and Consonants
# Write a program with a function that accepts a string as an argument and returns the
# number of vowels that the string contains. The application should have another function
# that accepts a string as an argument and returns the number of consonants that the string
# contains. The application should let the user enter a string, and should display the number
# of vowels and the number of consonants it contains.

def vowels(myString):
    vowel = 0
    for i in myString:
        letter = i.lower()
        if letter.isalpha():
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
                vowel += 1
    return vowel


def consonants(myString):
    consonant = 0
    for i in myString:
        letter = i.lower()
        if letter.isalpha():
            if letter != 'a' or letter != 'e' or letter != 'i' or letter != 'o' or letter != 'u':
                consonant += 1
    return consonant


def main():
    myString = input("Enter your string: ")
    vowel = vowels(myString)
    consonant = consonants(myString)
    print("The number of vowels: ", vowel)
    print("The number of consonants: ", consonant)


if __name__ == '__main__':
    main()
