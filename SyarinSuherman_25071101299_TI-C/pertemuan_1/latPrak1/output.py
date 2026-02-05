# --- BAB: OUTPUT ---

# 1. Output Dasar
print("Ini adalah output standar.")

# 2. Output Multiple Arguments
# Menggabungkan beberapa nilai dengan koma (otomatis diberi spasi)
print("Ayam", "Bebek", "Angsa")

# 3. Mengatur Separator (sep)
# Mengganti pemisah default (spasi) dengan karakter lain
print("01", "02", "2026", sep="-") # Output: 01-02-2026

# 4. Mengatur Akhiran (end)
# Secara default print() diakhiri baris baru (\n). Kita bisa menggantinya.
print("Kalimat satu.", end=" ")
print("Kalimat dua (masih di baris yang sama).")