## CLASS
# 1
class mobil:
    pass

# 2
class mobil:
    # Atribut
    warna = "merah"

## OBJECT(OBJEK) => Untuk memanggil kelas yang telah dibuat, kita membuat sebuah objek
# 1
class Mobil:
    # Atribut
    warna = "Merah"
 
mobil_1 = Mobil()

# 2 
# kita memanggil atribut objek yang berasal dari kelas Mobil, yaitu "Merah".
class Mobil:
    # Atribut
    warna = "Merah"

mobil_1 = Mobil() # mobil_1 => nama objek
print(mobil_1.warna) # .warna => nama atribut
"""
Output:
Merah
"""

# 3
# kita bisa mengubah nilai atribut yang ada di dalam kelas
class Mobil:
    # Atribut
    warna = 'Merah'

mobil_1 = Mobil()
mobil_1.warna = "Biru"
print(mobil_1.warna)
"""
Output:
Biru
"""

## ATRIBUT
# 1
class mobil:
    warna = "merah"

mobil_1 = mobil()
print(mobil_1.warna)

mobil_2 = mobil()
print(mobil_2.warna)

mobil.warna = "hitam"

print(mobil_1.warna)
print(mobil_2.warna)
"""
Output:
merah
merah
hitam
hitam
"""

## CLASS CONSTRUCTOR
# class constructor adalah sebuah fungsi khusus dalam Python yang digunakan untuk menentukan nilai awal atau kondisi awal dari suatu kelas.
# 1
class Mobil:
    def __init__(self):
        self.warna = 'Merah'
# Ini artinya ketika Anda membuat instance baru bernama "mobil_1", constructor akan dipanggil pertama kali dan self akan merujuk pada instance atau objek "mobil_1" tersebut. Begitu pun kalau kita membuat instance baru lainnya bernama "mobil_2", constructor akan dipanggil pertama kali dan self akan merujuk pada instance "mobil_2". Hal ini memungkinkan setiap objek baru tersebut memiliki atribut masing-masing, tidak lagi atribut kelas. Jadi, kita dapat mengubah atribut suatu objek tanpa memengaruhi objek lainnya. 

# 2
class Mobil:
    # Atribut Instance
    def __init__(self):
        self.warna = 'Merah'
        
mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# Mengubah atribut instance
mobil_1.warna = "Hitam"

# Menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna)
"""
Output:
Merah
Merah
Hitam
Merah
"""

# 3
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
        
mobil_1 = Mobil('Merah', 'DicodingCar', 160)

print(mobil_1.warna)
print(mobil_1.merek)
print(mobil_1.kecepatan)
"""
Output:
Merah
DicodingCar
160
"""

## METHOD
# 1. dekorator => Dekorator adalah fungsi dalam Python yang mengembalikan fungsi lain, biasanya diawali dengan sintaks "@" di awal
def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

# Dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("Hello, world!")

# Memanggil fungsi yang sudah didekorasi
say_hello()
"""
Output:
Sebelum fungsi dieksekusi.
Hello, world!
Setelah fungsi dieksekusi.
"""

# 2. Metode dari Objek (Object Method)
# 1 
class Mobil:
    # constructor
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    # method
    def menambah_kecepatan(self):
        self.kecepatan += 10
    
mobil_1 = Mobil("Merah", "Lamborgini", 60)
print(f"Kecepatan Mobil Sebelum adalah {mobil_1.kecepatan}km/jam")

mobil_1.menambah_kecepatan()
print(f"Kecepatan Mobil Setelah adalah {mobil_1.kecepatan}km/jam")
        