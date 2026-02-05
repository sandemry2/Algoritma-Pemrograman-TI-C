# FOR LOOPS
# digunakan untuk mengulang suatu urutan (baik berupa list, tuple, dictionary, set, atau string)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
print('\n')


# LOOPING STRING
# Loop huruf di kata 'banana'
for x in "banana":
  print(x)
print('\n')


# BREAK STATEMENT
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == 'banana':
    break
print('\n') # break setelah print banana

for x in fruits:
  if x == 'banana':
    break
  print(x) # break tanpa ngeprint banana
print('\n')


# CONTINUE STATEMENT
# menghentikan iteration loop saat ini, dan melanjutkan berikutnya
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) # tidak print banana
print('\n')


# THE RANGE() FUNCTION
# Fungsi ini range()mengembalikan serangkaian angka, dimulai dari 0 secara default, dan bertambah 1 (secara default), dan berakhir pada angka yang ditentukan
for x in range(6):
  print(x)
print ('\n')

# menentukan nilai awak dan akhir menggunakan parameter
for x in range (2, 5):
  print (x)
print('\n') #print 2, 3, 4

# menentukan nilai penambahan dengan paramater ketiga
for x in range(3, 20, 3):
  print (x)
print('\n')


# ELSE STATEMENT
for x in range(1, 8):
   if (x % 2 == 0):
    print(f'{x} adalah genap')
   else:
    print(f'{x} adalah ganjil')
print('\n')


# BREAK
# blok else tidak akan dieksekusi jika loop dihentikan oleh pernyataan break
for x in range (6):
  if x == 3: break
  print (x)
else:
  print ('Selesai')
print ('\n')


# PENGULANGAN BERSARANG/NESTED LOOP
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# PASS STATEMENT
# for loop tidak boleh kosong, tapi jika diperlukan for ;oop tanpa isi, tambahkan PASS 
for x in [0, 1, 2, 3]:
  pass