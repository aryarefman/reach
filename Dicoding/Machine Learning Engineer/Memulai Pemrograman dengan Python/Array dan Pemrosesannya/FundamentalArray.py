## list isinya bisa berbeda-beda tipe data, sedangkan array isinya hanya 1 tipe data
# 1 (menggunakan list sebagai array)
x = [1, 2, 3, 4, 5]
print(x)
"""
Output:
[1, 2, 3, 4, 5]
"""

# 2 (benar" menggunakan array dari library)
import array
x = array.array('i', [1, 2, 3, 4, 5])
print(x)
print(type(x))
"""
Output:
array('i', [1, 2, 3, 4, 5]) -> i: beritipe integer
<class 'array.array'>
"""

# 3
siswa = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60]
print(siswa)
print(siswa[0])
"""
Output:
[90, 100, 50, 80, 85, 45, 80, 75, 50, 60]
90
"""

