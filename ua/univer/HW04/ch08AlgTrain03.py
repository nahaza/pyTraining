# 3. Write a loop that counts the number of alphanumeric characters (letters or digits) that
# appear in the string referenced by mystring.

count = 0
mystring = 'df knn7 klk'
for x in mystring:
    if x.isalnum():
        count += 1
print(count)


# 3. Напишите цикл, который подсчитывает количество цифр в строковом значении, на которое ссылается mystring.

count = 0
mystring = 'df knn7 klk'
for x in mystring:
    if x.isdigit():
        count += 1
print(count)
