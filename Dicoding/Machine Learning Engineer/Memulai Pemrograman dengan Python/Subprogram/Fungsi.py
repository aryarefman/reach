## Mendefinisikan Fungsi dalam Python
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

## Memanggil Fungsi
# 1
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang
mencari_luas_persegi_panjang(10,5)   # Ini adalah pemanggil fungsi

# 2
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang
persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)
"""
Output:
50
"""

## Docstring
def mencari_luas_persegi_panjang(panjang,lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """

    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

"""
Output:
50
"""

## Argumen dan Parameter
# Argumen
# 1. keyword argument
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(lebar=10, panjang=5)

print(persegi_panjang_pertama)
"""
Output:
50
"""

# 2. positional argument
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)

print(persegi_panjang_pertama)
"""
Output:
50
"""

# Parameter
# 1. Positional-or-Keyword
def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))
"""
Output:
Halo, Dicoding! Selamat pagi!
Halo, Dicoding! Selamat sore!
"""

# 2. Positional-Only
def penjumlahan(a, b, /):
    return a + b

print(penjumlahan(8, 50))
"""
Output:
58
"""

# 3. Keyword-Only
def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting(pesan="Selamat sore!",nama="Dicoding"))
"""
Output:
Halo, Dicoding! Selamat sore!
"""

# 4. Var-Positional (Variadic Positional Parameter)
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))
"""
Output:
<class 'tuple'>
6
"""

# 5. Var-Keyword (Variadic Keyword Parameter)
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))
"""
Output:
nama: Dicoding, usia: 17, pekerjaan: Python Programmer,
"""

## Fungsi Anonim (lambda function)
luas_persegi_panjang = lambda p, l: p*l
print(luas_persegi_panjang(3, 4))
"""
Output:
12
"""

## Latihan
# 1
def angka_terkecil(a,b):
    if a > b:
        return b
    elif a < b:
        return a
    else:
        return a
    
print(angka_terkecil(1, 2))

# 2
def angka_terkecil(*args):
    current = args[0]
    for i in range(len(args)):
        next = args[i]
        if current > next:
            current = next
        else:
            current
    return current
        
print(angka_terkecil(5, 4, 6, 3, 7, 2, 0, 14))
print(angka_terkecil(2, 2))