# WHILE LOOPS

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Output:
# 1
# 2
# 3
# While akan terus melakukan perulangan selama i kurang dari 6. Tetapi
# keyword break membuat perulangan terhenti pada saat i samadengan 3.

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Output:
# 1
# 2
# 4
# 5
# 6
# While akan terus melakukan perulangan selama i kurang dari 6. Tetapi
# keyword continue membuat perulangan melewati print pada saat i samadengan 3.