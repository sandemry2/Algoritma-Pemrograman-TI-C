i = 1
while i < 8:
  print(i)
  i += 1 #akan mencetak i selama i kurang dari 8

#break
i = 1
while i < 6:
  print(i)
  if i == 4:
    break # break akan menghentikan looping ketika i bernilai 4
  i += 1

#continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue # continue akan melanjutkan ke iterasi berikutnya jika i adalah 3
  print(i)

#else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")