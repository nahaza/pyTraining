arr = [1, 23, 4, 5, 6, 7]
for value in arr:
    value += 1
    print(value)

for i in range(0, len(arr), 1):
    arr[i] +=2
    print("arr[", i, "] =", arr[i])
