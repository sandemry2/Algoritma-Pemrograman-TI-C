#Tipe data Boolean mewakili salah satu dari dua nilai: Benar atau Salah.
'''Saat kita menjalankan suatu kondisi dalam pernyataan if, 
Python akan mengembalikan nilai True atau False.'''

#contoh penggunaan boolean dalam pernyataan if
a = 200
b = 33

if b > a:
  print("b lebih besar dari a")
else:
  print("b tidak lebih besar dari a")

  '''Fungsi bool() memungkinkan Anda untuk mengevaluasi nilai apa pun, 
  dan memberikan hasil True atau False.'''
print(bool("Hello"))  #mengembalikan True karena string tidak kosong
print(bool(15))       #mengembalikan True karena angka tidak nol

print(bool(""))       #mengembalikan False karena string kosong
print(bool(0))        #mengembalikan False karena angka nol

#Beberapa nilai dianggap False secara default, seperti:
'''1. None
2. False
3. Angka nol dari semua tipe numerik, misalnya 0, 0.0, 0j.
4. Kumpulan data kosong seperti '', (), [], {}.'''
#Contoh nilai yang dianggap False
print(bool(None))    #mengembalikan False
print(bool(0))       #mengembalikan False
print(bool(()))      #mengembalikan False
print(bool([]))      #mengembalikan False
print(bool({}))      #mengembalikan False
print(bool(False))   #mengembalikan False
