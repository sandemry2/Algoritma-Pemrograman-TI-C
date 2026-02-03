#Operator digunakan untuk melakukan operasi pada variabel dan nilai.

#1. Arithmetic Operators
a = 10
b = 3
print(a + b)  #penjumlahan
print(a - b)  #pengurangan
print(a * b)  #perkalian
print(a / b)  #pembagian
print(a % b)  #modulus
print(a ** b) #pangkat
print(a // b) #pembagian lantai

#2. Assignment Operators

c = 5
c += 3  #sama dengan c = c + 3
print(c)

c -= 2  #sama dengan c = c - 2
print(c)

c *= 4  #sama dengan c = c * 4
print(c)

c /= 2  #sama dengan c = c / 2
print(c)

c %= 3  #sama dengan c = c % 3
print(c)

c **= 2 #sama dengan c = c ** 2
print(c)

c //= 3 #sama dengan c = c // 3
print(c)

#3. Comparison Operators
'''Operator perbandingan digunakan untuk membandingkan dua nilai
dan mengembalikan nilai Boolean (True atau False).'''

x = 10
y = 5
print(x == y)  #sama dengan
print(x != y)  #tidak sama denga
print(x > y)   #lebih besar dari
print(x < y)   #lebih kecil dari
print(x >= y)  #lebih besar dari atau sama dengan
print(x <= y)  #lebih kecil dari atau sama dengan

#4. Logical Operators
#Operator logika digunakan untuk menggabungkan pernyataan logika.

a = True
b = False
print(a and b)  #mengembalikan True jika kedua pernyataan benar
print(a or b)   #mengembalikan True jika salah satu pernyataan benar
print(not a)    #mengembalikan True jika pernyataan salah
print(not b)    #mengembalikan True jika pernyataan benar

#5. Membership Operators
#Operator keanggotaan digunakan untuk menguji apakah suatu nilai ada dalam sebuah urutan (seperti string, list, atau tuple).
mylist = [1, 2, 3, 4, 5]
print(3 in mylist)    #mengembalikan True karena 3 ada dalam mylist
print(6 not in mylist) #mengembalikan True karena 6 tidak ada dalam mylist

#6. Identity Operators
#Operator identitas digunakan untuk membandingkan objek, bukan nilai mereka.
a = ["apple", "banana"]
b = a
c = ["apple", "banana"]
print(a is b)      #mengembalikan True karena b adalah referensi ke a
print(a is c)      #mengembalikan False karena a dan c adalah objek yang berbeda
print(a is not c)  #mengembalikan True karena a dan c adalah objek yang berbeda /alamat memori nya :|
#berbeda meskipun memiliki nilai yang sama

#7. Bitwise Operators
#Operator bitwise digunakan untuk melakukan operasi pada level bit.
x = 5  #dalam biner: 0101
y = 3  #dalam biner: 0011
print(x & y)  #AND bitwise: 0001 (1 dalam desimal
print(x | y)  #OR bitwise:  0111 (7 dalam desimal)
print(x ^ y)  #XOR bitwise: 0100 (4 dalam desimal)
print(~x)     #NOT bitwise: 1010 (-6 dalam desimal)
print(x << 1) #Left shift:  1010 (10 dalam desimal
print(x >> 1) #Right shift: 0010 (2 dalam desimal)
