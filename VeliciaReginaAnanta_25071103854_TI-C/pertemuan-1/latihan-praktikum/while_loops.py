# While loops mengeksekusi perintah selama kondisinya terpenuhi (true)
i = 1
while i < 5:
   print(i)
   i += 1
print('\n')
# dibutuhkan pendefinisian sebuah indeks variabel, i, yang di set ke 1

# BREAK statement
# dengan BREAK kita dapat menghentikan loop bahkan saat kondisinya true
j = 1
while j < 6:
   print(j)
   if j == 3:
      break
   j += 1
print('\n')

#CONTINUE statement
# dengan CONTINUE, kita dapat memberhentikan iteration saat ini dan melanjutkan yang selanjutnya
k = 0
while k < 6:
   k += 1
   if k == 3:
      continue
   print(k)
print('\n')

# ELSE statement
# menjalankan blok code saat kondisi tidak terpenuhi
l = 1
while l < 6:
   print(l)
   l+= 1
else:
   print("l sudah melebihi 6")
# blok ELSE tidak akan dieksekusi ika loop berhenti dengan BREAK statement