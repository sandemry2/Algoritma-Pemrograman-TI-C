# --- BAB: IF ELSE ---

nilai = 75

# 1. Struktur Dasar
if nilai > 80:
    print("Nilai A")
elif nilai > 70:
    print("Nilai B") # Ini yang akan dieksekusi
else:
    print("Nilai C")

# 2. Short Hand If ... Else (Ternary Operator)
a = 200
b = 33
print("A") if a > b else print("B")

# 3. Nested If (If di dalam If)
x = 41
if x > 10:
    print("Diatas 10,")
    if x > 20:
        print("dan juga diatas 20!")