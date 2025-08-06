## len()
# List
contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(contoh_list)
print(len(contoh_list))
"""
Output:
[1, 3, 3, 5, 5, 5, 7, 7, 9]
9
"""

# Set
contoh_list = set([1, 3, 3, 5, 5, 5, 7, 7, 9])
print(contoh_list)
print(len(contoh_list))
"""
Output:
{1, 3, 5, 7, 9}
5
"""

# String
contoh_list = "Belajar Python"
print(contoh_list)
print(len(contoh_list))
"""
Output:
Belajar Python
14
"""

## min() dan max()
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))
"""
Output:
5
96
"""

## count()
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))
"""
Output:
3
"""

string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))
"""
Output:
6
"""

## in dan not in
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)
"""
Output:
True
False
False
True
"""

## Memberikan Nilai untuk Multiple Variable
data = ['shirt', 'white', 'L']
apparel = data[0]
color = data[1]
size = data[2]
# Alih-alih melakukannya satu persatu, Anda dapat melakukan hal tersebut sekaligus dalam Python
data = ['shirt', 'white', 'L']
apparel, color, size = data
print(data)
print(apparel)
print(color)
print(size)
"""
Output:
['shirt', 'white', 'L']
shirt
white
L
"""

## sort()
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)
"""
Output:
['helikopter', 'mobil', 'motor', 'pesawat']
"""
# 1. Membalikkan urutan
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)
print(kendaraan)
"""
Output:
['pesawat', 'motor', 'mobil', 'helikopter']
"""

# 2. Metode sort tidak dapat mengurutkan list yang memiliki angka dan string sekaligus di dalamnya
urutan = ['Dicoding', 1, 2, 'Indonesia', 3]
urutan.sort()
print(urutan)
"""
Output:
TypeError: '<' not supported between instances of 'int' and 'str'
"""

# 3. Metode sort menggunakan urutan ASCII sehingga nilai huruf kapital (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase)
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()
print(kendaraan)
"""
Output:
['Pesawat', 'helikopter', 'mobil', 'motor']
"""