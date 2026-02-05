# --- BAB: CASTING ---

# 1. Ke Integer
x = int(1)      # tetap 1
y = int(2.8)    # menjadi 2 (dibulatkan ke bawah)
z = int("3")    # string "3" menjadi angka 3

# 2. Ke Float
a = float(1)     # menjadi 1.0
b = float("4.2") # menjadi 4.2

# 3. Ke String
c = str("s1")   # tetap "s1"
d = str(2)      # angka 2 menjadi "2"
e = str(3.0)    # float 3.0 menjadi "3.0"

print(x, y, z)
print(a, b)
print(type(d)) # Sekarang d adalah string