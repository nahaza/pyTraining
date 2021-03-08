# 2. Write a loop that counts the number of space characters that appear in the string referenced by mystring.

mystring = 'df knn klklhhd n n  mnn mnbkj'
count = 0
for x in mystring:
    if x == " ":
        count += 1
print(count)

mystring = 'df knn klklhhd n n  mnn mnbkj'
count = 0
for x in mystring:
    if x.isspace():
        count += 1
print(count)
