#function arguments

def tambah(a, b):
    return a + b

print(tambah(1, 2)) # return 3

#function arguments with default value
def tambah(a, b=2):
    return a + b

print(tambah(1)) # return 3

#function arguments with *args
def tambah(*args):
    return sum(args)

print(tambah(1, 2, 3, 4, 5)) # return 15

#function arguments with **kwargs
def tambah(**kwargs):
    return sum(kwargs.values())

print(tambah(a=1, b=2, c=3, d=4, e=5)) # return 15

#function arguments with *args and **kwargs
def tambah(*args, **kwargs): 
    return sum(args) + sum(kwargs.values())

print(tambah(1, 2, 3, 4, 5, a=1, b=2, c=3, d=4, e=5)) # return 30, karena *args mengambil nilai positional dan **kwargs mengambil nilai keyword

#function scope
def tambah(a, b):
    return a + b

print(tambah(1, 2)) # return 3

#function declaration
def tambah(a, b):
    return a + b

print(tambah(1, 2)) # return 3

#function lambda
tambah = lambda a, b: a + b
print(tambah(1, 2)) # return 3

#python recursive function
def tambah(a, b):
    if b == 0:
        return a
    else:
        return tambah(a, b - 1)

print(tambah(1, 2)) # return 3

#function generators
def tambah(a, b):
    yield a + b

print(tambah(1, 2)) # return 3