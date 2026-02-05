##python booleans
#nilai boolean (true or false)
print(10 > 9)
print(10 == 9)
print(10 < 9)

#apabila menggunakan pernyataan if
a = 200
b = 33

if b > a:
  print("b lebih besar dari a")
else:
  print("b tidak lebih besar dari a")

#mengevaluasi nilai dan variabel
print(bool("Hello"))
print(bool(15))

#mengevaluasi dua variabel
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#sebagian besar nilai benar
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#beberapa nilai salah
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#fungsi yang mengembalikan nilai boolean 
def myFunction() :
  return True

print(myFunction())

#mengeksekusi kode berdasarkan jawaban boolean dari suatu fungsi
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#menentukan apakah suatu objek memiliki tipe data tertentu
x = 200
print(isinstance(x, int))



