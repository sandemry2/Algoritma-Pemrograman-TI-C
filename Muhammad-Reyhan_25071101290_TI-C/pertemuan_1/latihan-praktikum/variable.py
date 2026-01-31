# PYTHON VARIABLE

a = str(3) # string "3"
b = int(3) # integer 3
c = float(3) # floar 3.0

# python sensitif, a dan A itu berbeda
a = 3
A = 4
print(a, A)

# VARIABLE NAME

# legal
userId = 12345
useriD = 65213
user_id = 1231
_userId = 1234
userId1 = 1234
# illegal
2userId = 1234
user-id = 1234
user id = 123

# MULTIPLE VALUE
a, b, c = "Dimas", "Makan", "Ayam"
print(a, b, c)

# collection
nama = ["Dimas", "Indah", "Wawan"]
a, b, c = nama
print(a,b,c)

# GLOBAL VARIABLE

def tambah(a, b):
    a, b = 1, 3
    print(a,b)
    return a+b

def kurang(a, b):
    a, b = 1, 3
    print(a, b)
    return a-b

a = 10
b = 5
tambahh = tambah(a,b)
kurangg = kurang(a,b)
print(f"Penjumlahan dari {a}+{b} = {tambahh}")
print(f"Pengurangan dari {a}-{b} = {kurangg}")


