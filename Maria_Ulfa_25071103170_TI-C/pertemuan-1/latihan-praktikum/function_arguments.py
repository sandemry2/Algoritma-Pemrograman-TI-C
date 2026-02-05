##python function
"""Fungsi adalah blok kode yang hanya berjalan ketika dipanggil.
Fungsi dapat mengembalikan data sebagai hasilnya.
Fungsi membantu menghindari pengulangan kode."""

#membuat fungsi
"Dalam Python, fungsi didefinisikan menggunakan kata kunci, diikuti dengan nama fungsi dan tanda kurung: def"
def my_function():
  print("Hello from a function")

#memanggil fungsi: tulis nama fungsu diikuti dengan tanda kurung
def my_function():
  print("Hello from a function")

my_function()

#nama fungsi
"""Nama fungsi harus dimulai dengan huruf atau garis bawah
Nama fungsi hanya dapat berisi huruf, angka, dan garis bawah
Nama fungsi peka huruf besar/kecil ( dan berbeda)myFunctionmyfunction"""

#contoh fungsi yang valid
"""calculate_sum()
_private_function()
myFunction2()"""

#mengembalikan nilai
"Fungsi dapat mengirim data kembali ke kode yang memanggilnya menggunakan pernyataan.return"
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

#pernyataan pass
def my_function():
  pass


##function argumen
#fungsi dengan satu argumen
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#parameter vs argumen
"yaitu informasi yang diteruskan ke dalam fungsi"
def my_function(name): 
  print("Hello", name)

my_function("Emil") 

#jumlah argumen
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#nilai parameter default
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#argumen kata kunci
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

#argumen posisi
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

#mencampur argumen posisi dan kata kunci
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

#meneruskan tipe data yang berbeda
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#mengembalikan nilai
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

#mengembalikan tipe data yang berbeda
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#argumen khusus posisi
def my_function(name, /):
  print("Hello", name)

my_function("Emil")


#argumen khusus kata kunci
def my_function(name):
  print("Hello", name)

my_function("Emil")

#Menggabungkan Positional-Only dan Keyword-Only menggunakan: /*
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

