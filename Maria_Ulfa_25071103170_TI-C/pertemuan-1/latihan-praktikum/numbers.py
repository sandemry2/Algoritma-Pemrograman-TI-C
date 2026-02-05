##python numbers
#jenis angka dalam python
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#untuk melihat tipe angka dalam python
print(type(x))
print(type(y))
print(type(z))

#int: bilangan bulat positif/negatif, dengan panjang tidak terbatas
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#float:  angka yang bernilai desimal, angka ilmiah dengan huruf "e" yang menunjukkan pangkat 10
x = 1.10
y = 12E4
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#complex: ditulis dengan "j" sebagai bagian imajiner
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#untuk mengubah tipe data gunakan: :int() float() complex()
x = 1    
y = 2.8 
z = 1j  #bilangan complex tidak dapat diubah ke bilangan lain

a = float(x)
b = complex(y)
c = int(y)

print(a)
print(b)
print(c)

#untuk membuat angka acak gunakan: random() random
import random

print(random.randrange(1, 100))


