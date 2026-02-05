def hitung(a, b):
    # Fungsi hitung akan mengembalikan dua nilai sekaligus.
    return a + b, a - b

sum, sub = hitung(26, 8) # Dua variabel untuk menampung dua nilai kembalian.
print(f"Penjumlahan = {sum}")
print(f"Pengurangan = {sub}")