x = 6
print(type(x))
x = 6.0
print(type(x))
x = 1+2j
print(type(x))
"""
Output:
<class 'int'>
<class 'float'>
<class 'complex'>
"""

var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))
"""
Output:
10
140724505017048 <memory address>
11
140724505017080 <memory address>
ini artinya python tidak merubah isinya melainkan membuat variabel baru
"""

x = True
print(type(x))
x = False
print(type(x))
"""
Output:
<class 'bool'>
<class 'bool'>
"""

x = 'Dicoding'
print(type(x))
"""
Output: 
<class 'str'>
"""

multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum'at yang lalu."""
print(multi_line)
"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum'at yang lalu.
"""

x = 'Dicoding'
print(x[0])
""" 
Output:
D
"""

x = 'Dicoding'
x[0] = 'F'
""" 
Output:
TypeError: 'str' object does not support item assignment
"""

x = 'Dicoding'
print(x[2:])
"""
Output:
coding
"""

## Formatted String
name = "Perseus Evans"
print(f"Hello, nama saya {name}")
"""
Output: 
Hello, nama saya Perseus Evans
"""

## %-formating
name = "Perseus Evans"
print("Nama saya %s" % (name))
"""
Output: 
Nama saya Perseus Evans
"""

## str.format()
name = "Perseus Evans"
print("Nama saya {}".format(name))
"""
Output: 
Nama saya Perseus Evans
"""

## List
x = [1, 2.2, 'Dicoding']
print(type(x))
"""
Output: 
<class 'list'>
"""

x = [1, 'Dicoding', True, 1.0]
print(x[2])
""" 
Output:
True
"""

x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)
"""
Output:
['Indonesia', 2.2, 'Dicoding']
Nilai dalam suatu list bisa diubah (mutable)
"""

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(x[0])
print(x[2])
print(x[-1])
print(x[-3])
"""
Output:
laptop
mouse
microphone
keyboard
"""

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(x[0:5:2])
print(x[1:])
print(x[:3])
"""
Output:
['laptop', 'mouse', 'keyboard']
['monitor', 'mouse', 'mousepad', 'keyboard', 'webcam', 'microphone']
['laptop', 'monitor', 'mouse']
"""

## Tuple
x = (1, "Dicoding", 1+3j)
print(type(x))
"""
Output:
<class 'tuple'>
"""

x = (5, 'program', 1+3j)
print(x[1])
print(x[0:3])
""" 
Output:
program
(5, 'program', (1+3j))
"""

x = (5, 'program', 1+3j)
x[1] = 'Dicoding'
"""
Output:
'tuple' object does not support item assignment
isi dari tuple tidak dapat diubah (imutable)
"""

## Set
x = {1,2,7,2,3,13,3}
print(x[0])
"""
Output:
'set' object is not subscriptable
di dalam set kita tidak bisa melakukan indexing
"""

x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))
"""
Output:
{1, 2, 3, 7, 13}
<class 'set'>
nilai dalam set tidak akan duplikat
"""

## Method
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1.union(set2)
print("Union:", union)
intersection = set1.intersection(set2)
print("Intersection:", intersection)
"""
Output:
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}
"""

## Dictionary
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(type(x))
"""
Output:
<class 'dict'>
"""

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(x[0])
""" 
Output:
KeyError: 0
"""

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(x ['name'])
""" 
Output:
Perseus Evans
"""

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
x ['Job'] = "Web Developer"
print(x)
"""
Output:
{'name': 'Perseus Evans', 'age': 20, 'isMarried': False, 'Job': 'Web Developer'}
"""

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
del x['isMarried']
print(x)
"""
Output:
{'name': 'Perseus Evans', 'age': 20}
"""

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
x ['name'] = "Dicoding"
print(x)
"""
Output:
{'name': 'Dicoding', 'age': 20, 'isMarried': False}
"""

## Konversi Tipe Data
print(float(5))
"""
Output:
5.0
"""

print(int(5.6))
print(int(-5.6)) 
""" 
Output:
5
-5
"""

print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))
"""
Output:
25
25
25.0
25.6
"""

print(int("1p"))
"""
Output:
ValueError: invalid literal for int() with base 10: '1p
"""

print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))
"""
Output:
{1,2,3}
(5,6,7)
['h','e','l','l','o']
"""

print(dict([[1,2],[3,4]]))
"""
Output:
{1:2, 3:4}
"""

print(dict([(3,26),(4,44)]))
"""
Output:
{3:26, 4:44}
"""