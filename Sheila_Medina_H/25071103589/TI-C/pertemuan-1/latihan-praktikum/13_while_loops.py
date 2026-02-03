#python loops
#Python memiliki dua perintah perulangan dasar:
'''perulangan while
perulangan for'''

#1. While Loops
'''Perulangan while akan terus mengeksekusi blok kode 
selama kondisi yang diberikan bernilai True.'''

x = 1
while x <= 5:  #selama x kurang dari atau sama dengan 5
    print(x)   #tampilkan nilai x
    x += 1     #tingkatkan nilai x sebesar 1 setiap iterasi
    
#2.break statement
'''Kadang-kadang kita mungkin ingin keluar dari loop sebelum kondisinya menjadi False.  
Kita dapat menggunakan pernyataan `break` untuk keluar dari loop 
sebelum kondisinya menjadi False.'''

x = 1
while x <= 10:
    print(x)
    if x == 5:
        break
    x += 1

#3.continue statement
'''Dengan pernyataan `continue`, 
kita dapat menghentikan iterasi saat ini dan melanjutkan ke iterasi berikutnya.'''

x = 0
while x < 10:
    x += 1
    if x % 2 == 0:  #jika x adalah bilangan genap
        continue    #lewati iterasi ini
    print(x)        #tampilkan nilai x (hanya bilangan ganjil yang ditampilkan