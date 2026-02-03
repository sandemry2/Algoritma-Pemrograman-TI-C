
# Variabel digunakan untuk menyimpan data
# Python tidak perlu mendeklarasikan tipe data secara eksplisit

# 1. Contoh variabel dasar
x = 10              # integer
y = 3.14            # float
nama = "Shel"       # string
is_active = True    # boolean

print(x)
print(y)
print(nama)
print(is_active)

# 2. Mengubah nilai variabel
x = 20
print("Nilai x setelah diubah:", x)

# 3. Multiple assignment (satu baris, banyak variabel)
a, b, c = 1, 2, 3
print(a, b, c)

# 4. Satu nilai untuk banyak variabel
p = q = r = 100
print(p)
print(q)
print(r)

# 5. Mengetahui tipe data variabel
print(type(x))
print(type(nama))

# 6. Penggabungan string dan variabel
umur = 18
print("Nama saya", nama, "dan umur saya", umur)

# 7. Variabel Global

nilai = 5  # variabel global

def tambah_nilai():
    global nilai
    nilai += 5
    print("Nilai di dalam function:", nilai)

tambah_nilai()
print("Nilai di luar function:", nilai)
