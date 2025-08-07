# 1
matriks = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matriks)
"""
Output:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""

# 2
import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print(matriks)

"""
Output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

# 3 (numpy menggunakan lebih sedikit memori dibandingkan menggunakan list array)
import numpy 
import sys

var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array= numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])

print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)

"""
Output:
Ukuran keseluruhan elemen list dalam bytes =  240
Ukuran keseluruhan elemen NumPy dalam bytes =  72
"""