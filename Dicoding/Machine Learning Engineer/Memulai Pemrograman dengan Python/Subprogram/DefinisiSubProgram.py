## Tanpa SubProgram
# Luas pertama
panjang = 5
lebar = 10

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

# Luas kedua
panjang = 4
lebar = 15

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)
"""
Output:
50
60
"""

## Menggunakan SubProgram
def mencari_luas_persegi_panjang(p, l):
    return p * l

print(mencari_luas_persegi_panjang(5, 10))
print(mencari_luas_persegi_panjang(4, 15))