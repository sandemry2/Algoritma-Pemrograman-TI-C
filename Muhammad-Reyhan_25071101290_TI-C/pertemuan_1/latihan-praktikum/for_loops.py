#forloops

for i in range(5):
    print(f"Iterasi ke-{i}")

#for-else
for i in range(5):
    print(f"Iterasi ke-{i}")
else:
    print("Loop selesai.")

#for-break
for i in range(5):
    print(f"Iterasi ke-{i}")
    if i == 3:
        break

#for-continue
for i in range(5):
    i += 1
    if i == 3:
        continue
    print(f"Iterasi ke-{i}")

#for-pass
for i in range(5):
    i += 1
    if i == 3:
        pass
    print(f"Iterasi ke-{i}")

#for-nested
for i in range(5):
    for j in range(5):
        print(f"Iterasi ke-{i}-{j}")
