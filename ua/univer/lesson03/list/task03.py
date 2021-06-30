arr = [1, 23, 4, 5, 6, 7]
for value in arr:
    value += 1
    print(value)

for i in range(0, len(arr), 1):
    arr[i] +=2
    print("arr[", i, "] =", arr[i])

arr.append(10)
arr[2] = 3333
arr.insert(4, 8888)
for i in range(len(arr)):
    print("arr[", i, "] =", arr[i])

print(arr)

for value in arr:
    print(value)
