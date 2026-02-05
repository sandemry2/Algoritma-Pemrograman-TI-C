buah = ["mangga", "markisa", "pisang"]
for x in buah:
  print(x) 

for x in "banana":
  print(x) #akan melooping huruf dari banana

#The range() Function
for i in range(5):
    print(i)

for i in range(1, 6):   # range(1, 6) menghasilkan angka dari 1 sampai 5
    print(i)           # mencetak nilai i setiap perulangan

for i in range(0, 10, 2):  # mulai dari 0, berhenti sebelum 10, lompat 2
    print(i)              # mencetak 0, 2, 4, 6, 8

#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) # akan menampilkan setiap kata sifat untuk setiap buah