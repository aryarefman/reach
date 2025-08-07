# 1 (Mencari Nilai Terbesar)
var_arr = [1, 8, 10, 13, 2, 4, 37]
left_pointer = var_arr[0]

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)
"""
Output:
37
"""

# 2
var_array = [i for i in range(101)]
sum = 0
count = len(var_array)

for i in var_array:
    sum += i
    rata_rata = sum/count

print(rata_rata)