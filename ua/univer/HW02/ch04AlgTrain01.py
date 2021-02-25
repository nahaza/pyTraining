# Write a while loop that lets the user enter a number. The number should be multiplied
# by 10, and the result assigned to a variable named product. The loop should iterate as
# long as product is less than 100.

product = 0

while product < 100:
    number = int(input("Enter a number: "))
    product = number * 10
    print(product)

