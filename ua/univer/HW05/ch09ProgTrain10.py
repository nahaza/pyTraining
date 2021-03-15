# 10. Word Index
# Write a program that reads the contents of a text file. The program should create a dictionary in which the key-value pairs are described as follows:
# • Key. The keys are the individual words found in the file.
# • Values. Each value is a list that contains the line numbers in the file where the word
# (the key) is found.For example, suppose the word “robot” is found in lines 7, 18, 94, and 138. The dictionary
# would contain an element in which the key was the string “robot”, and the value was a list
# containing the numbers 7, 18, 94, and 138.
# Once the dictionary is built, the program should create another text file, known as a word
# index, listing the contents of the dictionary. The word index file should contain an alphabetical listing of the words that are stored as keys in the dictionary, along with the line
# numbers where the words appear in the original file. Figure 9-1 shows an example of an
# original text file (Kennedy.txt) and its index file (index.txt).