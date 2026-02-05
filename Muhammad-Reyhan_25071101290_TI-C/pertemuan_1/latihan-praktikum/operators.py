# arithmetic operators
x = 10
y = 20
print(x + y) # return 30
print(x - y) # return -10
print(x * y) # return 200
print(x / y) # return 0.5
print(x % y) # return 10
print(x ** y) # return 10240000000000000000
print(x // y) # return 0

# assignment operators
x = 10
y = 20
x += y # x = x + y
print(x) # return 30

x -= y # x = x - y
print(x) # return -10

x *= y # x = x * y
print(x) # return 200

x /= y # x = x / y
print(x) # return 0.5

x %= y # x = x % y
print(x) # return 10

x **= y # x = x ** y
print(x) # return 10240000000000000000

x //= y # x = x // y
print(x) # return 0

# comparison operators
x = 10
y = 20
print(x == y) # return False, karena x tidak sama dengan y
print(x != y) # return True, karena x tidak sama dengan y
print(x > y) # return False, karena x lebih kecil dari y
print(x < y) # return True, karena x lebih kecil dari y
print(x >= y) # return False, karena x lebih kecil dari y
print(x <= y) # return True, karena x lebih kecil dari y

# logical operators
x = 10
y = 20
print(x and y) # return 20, karena x dan y adalah integer
print(x or y) # return 10, karena x dan y adalah integer
print(not x) # return False, karena x adalah integer

# bitwise operators
x = 10
y = 20
print(x & y) # return 0, karena x dan y adalah integer
print(x | y) # return 30, karena x dan y adalah integer
print(x ^ y) # return 30, karena x dan y adalah integer
print(~x) # return -11, karena x adalah integer
print(x << y) # return 10485760, karena x adalah integer
print(x >> y) # return 0, karena x lebih kecil dari y

# identity operators
x = 10
y = 20
print(x is y) # return False, karena x tidak sama dengan y
print(x is not y) # return True, karena x tidak sama dengan y

# membership operators
x = 10
y = 20
print(x in y) # return False, karena x tidak ada di y
print(x not in y) # return True, karena x tidak ada di y

# operator precedence
x = 10
y = 20
z = 30
print(x + y * z) # return 610, karena perkalian didahulukan
print((x + y) * z) # return 900, karena penjumlahan didahulukan

# operator associativity
x = 10
y = 20
z = 30
print(x - y - z) # return -40, karena pengurangan didahulukan dari kiri
print(x - (y - z)) # return 20, karena pengurangan didahulukan dari kanan



