# OPERATORS
# OPERATOR ARITMATIKA

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
# Merupakan operator yang digunakan untuk melakukan operasi aritmatika seperti
# tambah (`+`), kurang (`-`), kali (`*`), bagi (`/`), dan hasil bagi (`%`)
# ============================================================================ #


# OPERATOR TUGAS

x = 5   # 5
x += 3  # 8 (5 + 3)
# Operator tugas adalah operator yang digunakan untuk memasukkan nilai
# ke dalam sebuah variabel, operator ini adalah kombinasi dari
# samadengan (`=`) dengan operator-operator lainnya.
# Operator Tugas Lengkap: https://www.w3schools.com/python/python_operators_assign.asp
# ============================================================================ #


# OPERATOR PERBANDINGAN

x = 5
y = 3

print(x == y)   # False
print(x != y)   # True
print(x > y)    # True
print(x < y)    # False
print(x >= y)   # True
print(x <= y)   # False
# Operator yang digunakan untuk membandingkan nilai operand.
# ============================================================================ #


# OPERATOR LOGIKA

x = 6
print(x > 0 and x < 10)         # True  | Operator and. Bernilai True jika kedua pernyataannya bernilai True.
print(x < 5 or x > 10)          # False | Operator or. Bernilai True jika minimal satu pernyataannya bernilai True.
print(not(x > 3 and x < 10))    # False | Operator not. Bernilai True jika pernyataannya bernilai False (kebalikan).
# ============================================================================ #


# OPERATOR IDENTITAS

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)   # True  | Operator is. Bernilai True jika objeknya sama (referensi di memory sama).
print(x is y)   # False | Jika objeknya sama, otomatis nilainya akan sama.
print(x == y)   # True  | Berbeda dengan operator == yang hanya membandingkan nilai.
# ============================================================================ #


# OPERATOR KEANGGOTAAN

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)           # True  | Operator in. Bernilai benar jika nilainya ada di dalam objek.
print("pineapple" not in fruits)    # True  | Operator not in. Bernilai benar jika nilainya tidak ada di dalam objek.
# ============================================================================ #


# OPERATOR BIT

# 6 = 0110
# 3 = 0011
print(6 & 3) # 2 | Jika sama-sama memiliki 1, maka akan digunakan. Jika tidak, maka 0. Hasil akhir: 0010.
print(6 | 3) # 7 | Jika salah satu memiliki 1, maka akan digunakan. Jika tidak, maka 0. Hasil akhir: 0111.
print(6 ^ 3) # 5 | Jika keduanya sama-sama 0 atau 1, maka 0. Jika tidak, maka 1. Hasil akhir: 0101.