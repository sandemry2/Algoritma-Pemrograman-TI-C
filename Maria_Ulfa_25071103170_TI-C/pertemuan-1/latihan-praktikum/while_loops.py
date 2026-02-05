##python while loops
#python loops
"terdiri dari 2, yaitu: while loop, dan for loop"

#lingkaran while
"Dengan perulangan while kita dapat mengeksekusi serangkaian pernyataan selama suatu kondisi benar."
i = 1
while i < 6:
  print(i)
  i += 1

#pernyataan break untuk menghentikan loop bahkan jika sementara kondisi benar
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#pernyataan continue untuk menghentikan iterasi saat ini
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#pernyataan else untuk menjalankan blok kode sekali ketika kondisi tidak lagi benar
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")





