#while loops

i = 0
while i < 5:
    print(f"Iterasi ke-{i}")
    i += 1

#while-else
i = 0
while i < 5:
    print(f"Iterasi ke-{i}")
    i += 1
else:
    print("Loop selesai.")

#while-break
i = 0
while i < 5:
    print(f"Iterasi ke-{i}")
    i += 1
    if i == 3:
        break

#while-continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(f"Iterasi ke-{i}")

#while-pass
i = 0
while i < 5:
    i += 1
    if i == 3:
        pass
    print(f"Iterasi ke-{i}")