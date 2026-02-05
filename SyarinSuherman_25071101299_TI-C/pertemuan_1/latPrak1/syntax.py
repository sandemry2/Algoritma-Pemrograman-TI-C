# --- BAB: SYNTAX ---
# Mencakup: Statement, Indentation, dan Struktur Dasar

# 1. Statement Sederhana
print("Hello, World!") 

# 2. Indentasi (Penting di Python!)
# Python menggunakan indentasi (spasi) untuk mendefinisikan blok kode, bukan kurung kurawal {}.
if 5 > 2:
    print("Lima lebih besar dari dua!") # Ini adalah blok indentasi
    print("Baris ini masih bagian dari if statement.")

# 3. Multi-line Statement (Menggunakan backslash)
total_perhitungan = 10 + \
                    20 + \
                    30
print("Total:", total_perhitungan)