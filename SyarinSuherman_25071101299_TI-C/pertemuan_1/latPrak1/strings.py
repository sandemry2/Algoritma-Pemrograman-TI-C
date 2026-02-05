# --- BAB: STRINGS ---

teks = "  Belajar Python  "

# 1. Slicing (Mengambil sebagian karakter)
print(teks[2:5]) # Mengambil index 2 sampai 4

# 2. Modifikasi String
print(teks.upper())         # HURUF BESAR
print(teks.lower())         # huruf kecil
print(teks.strip())         # Menghapus spasi di awal/akhir

# 3. Replace
print(teks.replace("Python", "Coding"))

# 4. F-String (Format String) - Sangat sering dipakai!
umur = 22
teks_format = f"Umur saya adalah {umur} tahun."
print(teks_format)