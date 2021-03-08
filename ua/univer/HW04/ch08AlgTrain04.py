# 4. Write a loop that counts the number of lowercase characters that appear in the string
# referenced by mystring.

count = 0
myString = "fgJJK kKfd TG dfkhdk"
for x in myString:
    if x.islower():
        count += 1
print(count)
