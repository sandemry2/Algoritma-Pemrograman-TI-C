# VARIABEL
# DEKLARASI

x = 2           # Tipe integer.
y = "Riyanda"   # Tipe string.
# Variabel bisa langsung dideklarasikan tanpa menentukan tipe data
# karena Python bersifat dinamis, tipe data ditentukan saat nilai diberikan.
# ============================================================================ #


# MELIHAT TIPE VARIABEL

print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>
# ============================================================================ #


# CASE SENSITIVE

X = 20              # Ini tidak akan menimpa isi dari variabel x,
Y = "Ahyaritama"    # Ini tidak akan menimpa isi dari variabel y.

print(x) # 2
print(y) # Riyanda
print(X) # 20
print(Y) # Ahyaritama
# Tidak tertimpa karena nama variabelnya berbeda antara huruf besar dan kecil
# sehingga komputer mendeklarasikan sebuah variabel baru.
# ============================================================================ #


# PENAMAAN

lowercase = "Benar"         # Semua huruf kecil.
snake_case = "Benar"        # Setiap kata dipisahkan underscore.
_underscorefirst = "Benar"  # Underscore didepan nama variabel.
camelCase = "Benar"         # Huruf pertama kecil, huruf awal kata selanjutnya besar.
PascalCase = "Benar"        # Huruf awal setiap kata besar.
UPPERCASE = "Benar"         # Semua huruf besar.
numberlast6 = "Benar"       # Angka diposisi terakhir.
# ============================================================================ #


# BANYAK NILAI DAN BANYAK VARIABEL

x, y, z = "Orange", "Banana", "Cherry"
print(x) # Orange
print(y) # Banana
print(z) # Cherry
# ============================================================================ #


# SATU NILAI DAN BANYAK VARIABEL

x = y = z = "Orange"
print(x) # Orange
print(y) # Orange
print(z) # Orange
# ============================================================================ #


# MENGURAI TUPLE DAN LIST
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x) # apple
print(y) # banana
print(z) # cherry
# ============================================================================ #


# OUTPUT

x = "Riyanda Ahyaritama"
print(x) # Riyanda Ahyaritama

y = "TI - C"
print(f"Nama: {x}, Kelas: {y}") # Nama: Riyanda Ahyaritama, Kelas: TI - C
# ============================================================================ #


# VARIABEL GLOBAL

# Variabel yang berada diluar scope manapun (tidak memiliki induk) atau
# variabel lokal yang diberi keyword `global` sehingga bisa diakses diluar
# induknya.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() # Python is awesome

# ================================== #

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) # Python is fantastic
# ============================================================================ #


