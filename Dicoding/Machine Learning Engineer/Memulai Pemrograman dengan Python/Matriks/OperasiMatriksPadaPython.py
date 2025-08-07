# Mengalikan Elemen Matriks
var_mat = [[5, 0],
           [1, -2]]
def_mat = [[0 for i in range(2)] for i in range(2)]

print(len(var_mat))

for i in range(len(var_mat)):
    for j in range(len(var_mat[0])):
        def_mat[i][j] = var_mat[i][j] * 2

print(def_mat)
"""
Output:
[[10, 0], [2, -4]]
"""

# lebih efektif menggunakan numpy
import numpy as np

var_mat = np.array([[5, 0],
                   [1, -2]])
result = var_mat*2

print(result)
"""
Output:
[[10  0]
 [ 2 -4]]
"""