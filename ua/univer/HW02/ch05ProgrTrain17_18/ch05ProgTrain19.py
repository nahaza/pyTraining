# 19. Prime Number List
# This exercise assumes that you have already written the is_prime function in Programming
# Exercise 17. Write another program that displays all of the prime numbers from 1 to 100.
# The program should have a loop that calls the is_prime function.

import isPrime

numMin = 1
numMax = 100


def main():
    for num in range(numMin, numMax + 1):
        if isPrime.isPrime(num):
            print(num)


main()
