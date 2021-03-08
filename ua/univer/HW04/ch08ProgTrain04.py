# 4. Morse Code Converter
# Morse code is a code where each letter of the English alphabet, each digit, and various
# punctuation characters are represented by a series of dots and dashes. Table 8-4 shows part
# of the code.
# Write a program that asks the user to enter a string, then converts that string to Morse code

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }


def main():
    inputString = input('Enter a string: ')

    for x in inputString:
        print(CODE[x.upper()], end=' ')


if __name__ == "__main__":
    main()
