## Mendeklarasikan Array
# 1
var_list = [1, 2, 3]
for i in var_list:
    print(id(i))
"""
Output:
140724948171192
140724948171224
140724948171256
"""

## Mendefinisikan Nilai Array
# 1
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)
"""
Output:
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""

## Mendefinisikan Nilai Default
# 1
var_arr = [0 for i in range(10)]
print(var_arr)
"""
Output:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""

# 2
var_list = [0 for i in range(10)]

for i in range(10):
    var_list[i] = i

print(var_list)
"""
Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

## Mengakses Elemen Array
# 1
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr[0])
"""
Output:
9
"""