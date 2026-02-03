# Contoh Penggunaan Struktur If...Else dalam Python

# 1️.Struktur Dasar
# "if" digunakan untuk mengeksekusi kode hanya jika kondisi True
x = 10
if x > 5:
    print("x lebih besar dari 5")  # dijalankan karena 10 > 5

# 2️.if...else
# "else" dijalankan jika kondisi if False
x = 3
if x > 5:
    print("x > 5")  # tidak dijalankan
else:
    print("x <= 5") # dijalankan karena 3 <= 5

# 3️.if...elif...else
# "elif" bisa dipakai untuk kondisi tambahan
x = 7
if x > 10:
    print(" x > 10")        # tidak dijalankan
elif x > 5:
    print("x > 5 tapi <= 10") # dijalankan karena 7 > 5
else:
    print(" x <= 5")        # tidak dijalankan

# Menggunakan operator logika
# Bisa gabungkan beberapa kondisi dengan "and", "or", "not"
x = 8
y = 3
if x > 5 and y < 5:  # kedua kondisi harus True
    print("x > 5 and < 5") # dijalankan

# Contoh kombinasi "or"
x = 4
y = 7
if x > 5 or y > 5:  # salah satu True saja cukup
    print("x > 5 or > 5") # dijalankan karena y > 5

# Menggunakan "not"
# "not" membalik nilai kondisi
if not x > 5:  # artinya x <= 5
    print("x <= 5 (not x >5)")  

#4. Nested If...Else
# Struktur if...else di dalam if...else lainnya

x = 12
if x > 10:
    if x < 15:
        print("10 < x < 15")  # dijalankan karena 12 di antara 10 dan 15
    else:
        print("x >= 15")