#variable dasar
x = 5
y = "John"
print(type(x))
print(type(y))
print("====================")
x = 4       # x is of type int
x = "Sally" # x is now of type str, program akan memproses sebagai variable x yang baru
print(x)

print("=========================================")
#nama variable, aturan penamaan memiliki banyak jenisnya. berikut adalah contohnya
myvar = "John" #lowercase
my_var = "John" #snake case
_my_var = "John"
myVar = "John" #camel case
MYVAR = "John"
myvar2 = "John"
MyVar = "John" #uppercase

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
print (MyVar)
#jika dalam formula terdapat kesalahan seperti spasi, 
#angka berada di depan, dan menggunakan karakter - maka akan terjadi error

print("=========================================")
#Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry" #ketiga variable memiliki identitas yang berbeda
print(x)
print(y)
print(z)
print("==============")
x = y = z = "Orange" #ketiga variable memiliki identitas yang sama
print(x)
print(y)
print(z)
print("==============")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits #fruits merupakan variable yang bernilai ketiga hal yang berbeda
print(x)            #ketika dimasukan ke xyz, maka akan masuk sesuai dengan urutannya
print(y)
print(z)

print("=========================================")
#Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#koma bisa diubah dengan karakter  tambah 
print("==============")
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#tambah sebagai operator matematika
print("==============")
x = 5
y = 10
print(x + y)
#tetapi tidak bisa kalau huruf + angka, jika ingin, hanya bisa pakai koma
print("==============")
x = 5
y = "John"
print(x, y)

print("=========================================")
#Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)
myfunc()

#bisa disambung dengan variable global lainnya
print("==============")
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

#bisa pakai global keyword juga
print("==============")
x = "awesome"

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
