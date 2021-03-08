# 6. Write code that makes a copy of a string with all occurrences of the lowercase letter
# 't' converted to uppercase.

myString = 'dfsdftdm gtntf'
whatToChange = 't'
newString = myString.replace(whatToChange, whatToChange.upper())
print(newString)