## Block Code
# 1
for i in range(10):
    print(i)
"""
Output:
0
1
2
3
4
5
6
7
8
9
"""

# 2
# for i in range(10):
# print(i)
"""
Output:
IndentationError: expected an indented block
"""

## Case-Sensitive
teks = "Dicoding"
Teks = "Indonesia"
print(teks)
print(Teks)
# print(TEks)
"""
Output:
Dicoding
Indonesia
NameError: name 'TEks' is not defined
"""