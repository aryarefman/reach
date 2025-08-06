## membuat sebuah kode hanya dalam satu baris saja atau berupa single statement

## cara umum
x = 1
y = 2

temp = x
x = y
y = temp

print("Setelah pertukaran: ")
print("x =", x)
print("y =",  y)
"""
Output:
Setelah pertukaran: 
x = 2
y = 1
"""

## cara one-liner
x = 1
y = 2

x, y = y, x    # One-liner

print('Setelah pertukaran: ')
print('x =', x)
print('y =', y)
"""
Output:
Setelah pertukaran: 
x = 2
y = 1
"""