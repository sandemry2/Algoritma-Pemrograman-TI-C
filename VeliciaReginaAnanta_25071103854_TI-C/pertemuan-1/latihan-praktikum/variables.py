# Variabel python tidak wajib di deklarasi
a = 5  # tipe int
b = 'semangka'  # tipe str

# Casting
x = int(3)  # 3
y = str(3)  # '3'
z = float(3)  # 3.0

# Tipe variabel
tinggi = 12
lebar = '9'
print(type(tinggi))
print(type(lebar))

# Case sensitive
num = 3
Num = 5
# num != Num, tidak akan terjadi overwrite

c, d, e = "Orange", "Banana", "Cherry"
print(c)
print(d)
print(e)

f = g = "Mawar"
print(f)
print(g)

# Unpacking a collection
hewan = ['kucing', 'anjing', 'kelinci']
h, i, j = hewan
print(h)
print(i)
print(j)

# Global Vaiabel
# variabel yang didefinisikan di luar fungsi
globalVar = 5
def cetakX():
    print(globalVar)
cetakX()

# Global Keyword
# If you use the global keyword, the variable belongs to the global scope
# To change the value of a global variable inside a function, refer to the variable by using the global keyword
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)
