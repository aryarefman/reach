## for
# 1
var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)
"""
Output:
1
2
3
4
5
6
7
8
9
10
"""

# 2
for i in range(10):
    print(i)
"""
Output:
1
2
3
4
5
6
7
8
9
10
"""

# 3 (range)
# range(start, stop, step)
for i in range(1,10,2):
    print(i)
"""
Output:
1
3
5
7
9
"""

## while
# 1
counter = 1
while counter <= 5:
    print(counter)
    counter+=1
"""
Output:
1
2
3
4
5
"""

## for bersarang
for i in range(1, 3):
    for j in range(1, 3):
        print(f"{i}, {j}")
"""
Output:
1,1
1,2
2,1
2,2
"""

### KONTROL PERULANGAN
# break
# 1
for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1
"""
Output:
Perulangan luar: 0
Perulangan dalam: 0
Perulangan dalam: 1
Perulangan luar: 1
Perulangan dalam: 0
Perulangan dalam: 1
"""

# 2
teks = "Dico ding"
for i in teks:
    if i == " ":
        break
    print(f"huruf saat ini: {i}")
"""
Output:
huruf saat ini: D
huruf saat ini: i
huruf saat ini: c
huruf saat ini: o
"""

# Continue
# 1
teks = "Dico ding"
for i in teks:
    if i == " ":
        continue
    print(f"huruf saat ini: {i}")
"""
Output:
huruf saat ini: D
huruf saat ini: i
huruf saat ini: c
huruf saat ini: o
huruf saat ini: d
huruf saat ini: i
huruf saat ini: n
huruf saat ini: g
"""

# else setelah for (mencari jalan keluar perogram ketika pencarian tidak ditemukan)
for i in range(5):
    if i+1 == 6:
        print(f"angka {i+1} ditemukan")
        break
else:
    print(f"angka tidak ditemukan!")
"""
Output:
angka tidak ditemukan!
"""

# else setelah while
count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")
"""
Output:
Dicoding Indonesia
Dicoding Indonesia
Dicoding Indonesia
Blok else dieksekusi karena kondisi pada while salah (3<3 == False).
"""

# else setela while (break)
n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")
"""
Output:
9
8
"""
# Pada contoh di atas, kita mencoba menampilkan angka dari 9 hingga 1. Program akan berhenti ketika angka tersebut adalah 7. Namun, lihat baik-baik bahwa else tidak tercetak di sini. Hal ini disebabkan while tersebut masih bernilai benar walaupun program keluar karena "break".

# pass
x = 10
if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")
"""
Output:

"""

# list Comprehension
# cara umum
angka = [1, 2, 3, 4, 5]
pangkat = []
for i in angka:
    pangkat.append(i**2)
print(pangkat)
"""
Output:
[1, 4, 9, 16, 25]
"""

# cara list comprehension
angka = [1, 2, 3, 4, 5]
pangkat = [i**2 for i in angka]
print(pangkat)
"""
Output:
[1, 4, 9, 16, 25]
"""

# evenNumber (0-500)
evenNumber = [i for i in range(0, 500) if i%2 == 0]
print(evenNumber)