#Boolean Values
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") #Cetak pesan berdasarkan apakah kondisinya benar Trueatau salah False

#Mengevaluasi Nilai dan Variabel
x = "Hello"
y = 15

print(bool(x))
print(bool(y)) #Fungsi ini bool()memungkinkan Anda untuk mengevaluasi nilai apa pun

print(bool("abc")) #akan false ketika string kosong
print(bool(123)) #akan false ketika diberi angka 0
print(bool(["apple", "cherry", "banana"])) #Semua list, tuple, set, dan dictionary adalah True, kecuali yang kosong

#nilai false pada booleans
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#Fungsi dapat Mengembalikan Nilai Boolean
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int)) #Periksa apakah suatu objek merupakan bilangan bulat atau bukan
