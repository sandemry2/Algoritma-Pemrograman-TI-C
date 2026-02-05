True or False

# True
print(bool(10 > 9))
print(bool(-1))
print(bool('Hy all'))
print(bool(' '))
listNum = [0]  # list, tuple, set (), [], {}
print(bool(listNum))

# False
print(bool(False))
print(bool(0))
print(bool(""))
listEmpty = []  # list, tuple, set (),[],{}
print(bool(listEmpty))
print(bool(()))
print(bool([]))
print(bool({}))

# Fungsi dapat mengembalikann nilai boolean


def myFunc():
    return True


print(myFunc())

# fungsi isinstance()
# Menentukan apakah sebuah objek merupakan tipe data teretentu
# isintance(objek, data type)
x = 200
print(isinstance(x, int))
print(isinstance(x, float))
