#python for loops
'''Perulangan `for` digunakan untuk mengulang suatu urutan 
(baik berupa daftar, tuple, kamus, himpunan, atau string).

Ini kurang mirip dengan kata kunci `for` dalam bahasa pemrograman lain,
 dan lebih mirip dengan metode iterator seperti yang ditemukan dalam 
 bahasa pemrograman berorientasi objek lainnya.

Dengan perulangan `for`, kita dapat mengeksekusi serangkaian pernyataan, 
satu kali untuk setiap item dalam daftar, tuple, himpunan, dan lain sebagainya.'''

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#1.Looping melalui string
#Kita juga dapat menggunakan perulangan `for` 
# untuk mengulang setiap karakter dalam string.
for x in "banana":
  print(x) 

#2.The break statement
'''Kita dapat menggunakan pernyataan `break` untuk keluar dari loop
    sebelum loop selesai secara alami.'''
print("\n")
for x in fruits:
  print(x)
  if x == "banana":
    break

#3.The continue statement
'''Dengan pernyataan `continue`,
    kita dapat menghentikan iterasi saat ini 
    dan melanjutkan ke iterasi berikutnya.'''
print("\n")
for x in range(6):
    if x == 3:
        continue
    print(x)

#4.The range() function
'''Fungsi `range()` menghasilkan deretan angka,
    yang sering digunakan dalam perulangan `for`.'''
print("\n")
#Mulai dari 0, hingga 6 (tidak termasuk 6)
for x in range(6):
    print(x)

#5.Else in for loop
'''Kita dapat menambahkan blok `else` setelah perulangan `for`.
    Blok `else` akan dieksekusi ketika loop selesai secara alami.'''
print("\n")
for x in range(7): #Mulai dari 0, hingga 7 (tidak termasuk 7)
    print(x) #tampilkan nilai x
else:
    print("Finally finished!") #tampilkan pesan setelah loop selesai

#6.Nested loops
'''Kita dapat menggunakan perulangan `for` di dalam perulangan `for`
    untuk membuat perulangan bersarang (nested loops).'''
print("\n")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
#7.Pass statement
'''Jika kita ingin membuat perulangan `for`
    tanpa isi, kita dapat menggunakan pernyataan `pass`
    untuk menghindari kesalahan sintaks.'''
print("\n")
for x in [0, 1, 2]:
    pass
