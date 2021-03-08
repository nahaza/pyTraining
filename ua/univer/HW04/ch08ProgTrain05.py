# 5. Alphabetic Telephone Number Translator
# Many companies use telephone numbers like 555-GET-FOOD so the number is easier for
# their customers to remember. On a standard telephone, the alphabetic letters are mapped to
# numbers in the following fashion:
# A, B, and C = 2
# D, E, and F = 3
# G, H, and I = 4
# J, K, and L = 5
# M, N, and O = 6
# P, Q, R, and S = 7
# T, U, and V = 8
# W, X, Y, and Z = 9
# Write a program that asks the user to enter a 10-character telephone number in the format XXX-XXX-XXXX.
# The application should display the telephone number with any
# alphabetic characters that appeared in the original translated to their numeric equivalent. For example,
# if the user enters 555-GET-FOOD, the application should display
# 555-438-3663.

def main():
    newNumber = ''
    nextDigit = ''
    telephNumber = input("Enter a 10-character telephone nextDigit in the format XXX-XXX-XXXX: ")
    for x in telephNumber:
        if x.isdigit():
            nextDigit = x
        elif x == '-':
            nextDigit = '-'
        elif x.isalpha():
            nextDigit = 1
            if x.lower() in "abc":
                nextDigit = 2
            elif x.lower() in "def":
                nextDigit = 3
            elif x.lower() in "ghi":
                nextDigit = 4
            elif x.lower() in "jkl":
                nextDigit = 5
            elif x.lower() in "mno":
                nextDigit = 6
            elif x.lower() in "pqrs":
                nextDigit = 7
            elif x.lower() in "tuv":
                nextDigit = 8
            elif x.lower() in "wxyz":
                nextDigit = 9
        newNumber += str(nextDigit)
    print(newNumber)


main()





