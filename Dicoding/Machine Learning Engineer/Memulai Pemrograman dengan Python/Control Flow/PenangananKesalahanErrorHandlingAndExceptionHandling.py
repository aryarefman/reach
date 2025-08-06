## Kesalahan Sintaks (Syntax Errors)
# 1
# if 9>10:
# print("Hello World!")
"""
Output:
File "/home/glot/main.py", line 2
    print("Hello World!")
    ^
IndentationError: expected an indented block
"""

# 2
# i = 1
# while i<3
#     print("Dicoding")
#     i+=1
"""
Output:
  File "/home/glot/main.py", line 2
    while i<3
             ^
SyntaxError: invalid syntax
"""

## Pengecualian (Exceptions)
# 1
# print(angka)
"""
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 1, in <module>
    print(angka)
NameError: name 'angka' is not defined
"""

# 2
# bukan_angka = '1'
# bukan_angka + 2
"""
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 2, in <module>
    bukan_angka + 2
TypeError: can only concatenate str (not "int") to str
"""

## Penanganan Pengecualian/Exception

# struktur sederhana
# try:
#     <Blok kode yang mungkin terjadi pengecualian>
# except:
#     <# Peryataan yang diberikan jika terjadi pengecualian>

# 1
z=0
try:
    print(1/z)
except ZeroDivisionError:
    print("Anda tidak bisa membagi angka dengan nilai nol.")
"""
Output:
Anda tidak bisa membagi angka dengan nilai nol.
"""

# struktur lengkap
# try:
#     <Blok kode yang mungkin terjadi pengecualian>
# except:
#     <Peryataan yang diberikan jika terjadi pengecualian>
# else:
#     <Pernyataan yang dioperasikan apabila tidak terjadi pengecualian>
# finally:
#     <Pernyataan yang dioperasikan setelah semua proses di atas terjadi>

# 2
var_dict = {"rata_rata": "1.0"}
try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")
"""
Output:
rata-rata adalah 1.0
Kode ini dieksekusi jika tidak ada exception.
Kode ini dieksekusi terlepas dari ada atau tidaknya exception.
"""

## Raise Exception (menangani kesalahan yang disengaja)
var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i+1)
"""
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 3, in <module>
    raise ValueError("Bilangan negatif tidak diperbolehkan")
ValueError: Bilangan negatif tidak diperbolehkan
"""