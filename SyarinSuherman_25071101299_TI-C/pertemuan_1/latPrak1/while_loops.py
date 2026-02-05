# --- BAB: WHILE LOOPS ---

i = 1

# 1. While standar
while i < 6:
    print(i)
    
    # 2. Break Statement
    if i == 3:
        print("Loop dihentikan saat i = 3")
        break 
    
    i += 1 # Jangan lupa increment agar tidak infinite loop

# 3. Continue Statement (Lewati iterasi)
j = 0
while j < 5:
    j += 1
    if j == 2:
        continue # Lewati angka 2, langsung ke loop berikutnya
    print("Nilai j:", j)