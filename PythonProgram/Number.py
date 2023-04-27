# Number
i = 89
print(float(i))
print(complex(i))
print(int(i))

i = 9.0234
print(float(i))
print(complex(i))
print(int(i))

# Who to find the Max and min Value

value = [10, 23, 56, 454, 0, 23]
print(max(value))
print(min(value))

arr = [5, 2, 8, 3, 9, 4]

max_num = arr[0]  # Initialize max_num to the first element of the array
for num in arr:
    if num > max_num:
        max_num = num
print("The maximum number is:", max_num)
