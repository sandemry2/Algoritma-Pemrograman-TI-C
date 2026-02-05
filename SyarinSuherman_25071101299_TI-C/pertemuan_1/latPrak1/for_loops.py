# --- BAB: FOR LOOPS ---

buahs = ["Apel", "Pisang", "Ceri"]

# 1. Loop melalui List
for buah in buahs:
    print(buah)

# 2. Loop melalui String
for huruf in "Python":
    print(huruf)

# 3. Range Function
# range(start, stop, step)
for x in range(2, 11, 2): # Mulai 2, sampai <11, lompat 2
    print(x) # Output: 2, 4, 6, 8, 10

# 4. Nested Loops
adj = ["Merah", "Besar"]
objects = ["Apel", "Tas"]

for x in adj:
    for y in objects:
        print(x, y)