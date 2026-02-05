# --- BAB: BOOLEANS ---

# 1. Nilai langsung
print(10 > 9)  # True
print(10 == 9) # False

# 2. Menggunakan fungsi bool()
# Hampir semua nilai bernilai True jika ada isinya
print(bool("Hello")) 
print(bool(15))

# Nilai yang dianggap False:
# (), [], {}, "", 0, None, False
print(bool(0))      # False
print(bool([]))     # False