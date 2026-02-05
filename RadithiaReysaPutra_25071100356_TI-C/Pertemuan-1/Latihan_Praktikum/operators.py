x = 15
y = 4

print(x + y)   # Penjumlahan: 15 + 4 = 19
print(x - y)   # Pengurangan: 15 - 4 = 11
print(x * y)   # Perkalian: 15 * 4 = 60
print(x / y)   # Pembagian: 15 / 4 = 3.75 (hasil float)
print(x % y)   # Modulus: sisa hasil bagi 15 / 4 = 3
print(x ** y)  # Perpangkatan: 15 pangkat 4 = 50625
print(x // y)  # Pembagian bulat: 15 // 4 = 3

#Assignment Operators
x = 5
print(x)     # Output: 5
x = 5
x += 3
print(x)     # Output: 8
x = 5
x -= 3
print(x)     # Output: 2
x = 5
x *= 3
print(x)     # Output: 15
x = 5
x /= 2
print(x)     # Output: 2.5
x = 5        # 101
x &= 3       # 011
print(x)     # Output: 1
x = 5        # 101
x |= 3       # 011
print(x)     # Output: 7
x = 5        # 101
x ^= 3       # 011
print(x)     # Output: 6
x = 8        # 1000
x >>= 2
print(x)     # Output: 2
x = 2        # 0010
x <<= 2
print(x)     # Output: 8
print(x := 3)   # Output: 3
print(x)        # Output: 3

#comparison 
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#operasi logika
x = 5
print(x > 3 and x < 10) #penggunaan and
x = 5
print(x > 3 or x < 4) #penggunaan or
x = 5
print(not(x > 3 and x < 10)) #penggunaan not
