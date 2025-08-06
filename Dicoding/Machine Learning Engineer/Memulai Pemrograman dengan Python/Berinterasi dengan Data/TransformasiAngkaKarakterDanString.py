## Mengubah Huruf Besar/Kecil
# 1. upper()
kata = 'dicoding'
kata = kata.upper()
print(kata)
"""
Output:
DICODING
"""

# 2. lower()
kata = 'DICODING'
kata = kata.lower()
print(kata)
"""
Output:
dicoding
"""

## Awalan dan Akhiran
# 1. r.strip() => Metode rstrip() menghapus whitespace pada sebelah kanan atau akhir string
print("Dicoding          ".rstrip())
"""
Output:
Dicoding
"""

# 2. lstrip() => lstrip() bertugas untuk menghapus whitespace pada sebelah kiri atau awal string
print("          Dicoding".lstrip())
"""
Output:
Dicoding
"""

# 3. strip => Metode ini bertugas untuk menghapus whitespace pada bagian awal dan akhir string
print("          Dicoding          ".strip())
"""
Output:
Dicoding
"""

# 4. Jika ingin menghilangkan karakter selain whitespace
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))
"""
Output:
Dicoding
"""

# 5. startswith() => Metode startswith() bertujuan untuk menemukan suatu kata pada awal string, metode ini mengembalikan nilai True/False
print('Dicoding Indonesia'.startswith("Dicoding"))
"""
Output:
True
"""

# 6. endswith() => Metode endswith() bertujuan untuk menemukan suatu kata pada akhir string, metode ini mengembalikan nilai True/False
print('Dicoding Indonesia'.endswith("Dicoding"))
"""
Output:
False
"""

## Memisah dan Menggabungkan String
# 1. join()
print(' '.join(['Dicoding', 'Indonesia', '!']))
"""
Output:
Dicoding Indonesia !
"""

# 2. Bisa juga menambahkan delimiter lain
print('123'.join(['Dicoding', 'Indonesia']))
"""
Output:
Dicoding123Indonesia
"""

# 3. split()
print('Dicoding Indonesia !'.split())
"""
Output:
['Dicoding', 'Indonesia', '!']
"""

# 4. Bisa juga menggunakan delimiter newline (\n) untuk memisahkan setiap baris pada string multiline
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))
"""
Output:
['Halo,', 'aku ikan,', 'aku suka sekali menyelam', 'aku tinggal di perairan.', 'Badanku licin dan renangku cepat.', 'Senang berkenalan denganmu.']
"""

## Mengganti Elemen String
# 1. replace()
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemograman"))
"""
Output:
Ayo belajar Pemograman di Dicoding
"""

## Pengecekan String
# 1. isupper()
kata = 'DICODING'
print(kata.isupper())
"""
Output:
True
"""
# 2. islower()
kata = 'dicoding'
print(kata.islower())
"""
Output:
True
"""

# 3. isalpha()
kata = 'dicoding'
print(kata.isalpha())
"""
Output:
True
"""

# 4. isalnum()
kata = 'dicoding123'
print(kata.isalnum())
"""
Output:
True
"""

# 5. isdecimal()
print('123'.isdecimal())
"""
Output:
True
"""

# 6. isspace()
print('    '.isspace())
"""
Output:
True
"""

# 7. istitle()
print('Dicoding Indonesia'.istitle())
"""
Output:
True
"""

## Formating pada String
# 1. zfill() => menambahkan angkan 0 didepan string
teks = 'Code'
tambah_number = teks.zfill(5)
print(tambah_number)
"""
Output:
0Code
"""

# 2. rjust => menambahkan elemen di depan string
print('Dicoding'.rjust(20))
"""
Output:
            Dicoding
"""

print('Dicoding'.rjust(20, '!'))
"""
Output:
!!!!!!!!!!!!Dicoding
"""

# 3. ljust() => menambahkan elemen di belakang string
print('Dicoding'.ljust(20))
"""
Output:
Dicoding            
"""

# 4. center() => menjadikan teks rata tengah
print('Dicoding'.center(10, '-'))
"""
Output:
-Dicoding-            
"""

## Stirng Literals
# st1 = 'Jum'at' => akan terjadi error
st1 = "Jum'at"
st1 = 'Jum\'at'
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")
"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum'at yang lalu.
"""

## Raw String => Python juga menyediakan cara untuk mencetak string sesuai dengan apa pun input atau teks yang diberikan
print(r'Dicoding\tIndonesia')
"""
Dicoding\tIndonesia
"""