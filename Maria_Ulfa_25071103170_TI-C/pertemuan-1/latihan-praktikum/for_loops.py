##python for loops
"Loop for digunakan untuk mengulangi urutan (yaitu daftar, tuple, kamus, himpunan, atau string)."

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#mengulang melalui string
for x in "banana":
  print(x)

#pernyataan break untuk menghentikan perulangan sebelum mengulang semua item
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#pernyataan continue untuk menghentikan iterasi loop saat ini, dan lanjutkan dengan yang berikutnya
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#fungsi range
"untuk mengulang serangkaian kode beberapa kali tertentu"
for x in range(6):
  print(x)

#menggunakan parameter start
for x in range(6):
  print(x)

#tingkatkan urutan dengan 3 (defaultnya adalah 1)
for x in range(2, 30, 3):
  print(x)

#else di for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#penggunaan else break
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#loop bersarang
"Perulangan bersarang adalah perulangan di dalam perulangan."
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#pernyataan pass
"for loop tidak bisa kosong, masukkan pernyataan untuk menghindari kesalahan forpass "
for x in [0, 1, 2]:
  pass



