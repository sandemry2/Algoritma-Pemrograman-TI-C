##python variables
#membuat variabel
x = 5
y = "saya"
print(x)
print(y)
#untuk menentukan tipe data variabel, lakukan dengan transmisi
x = str(2)
y = int(2)
z = float(2)
print(x); print(y); print(z)
#untuk melihat tipe data variabel, gunakan: type()
x = 5
y = "saya"
print(type(x)); print(type(y))
#variabel string dapat dideklarasikan dengan tanda kutip tunggal ataupun ganda
x = "saya"
print(x)
x = 'saya'
print(x)
#nama variabel peka huruf besar/kecil
a = 2
A = "saya"
print(a); print(A)


##variable names
#aturan pemberian nama variabel pada python
"""
>Nama variabel harus dimulai dengan huruf atau karakter garis bawah
>Nama variabel tidak dapat dimulai dengan angka
>Nama variabel hanya dapat berisi karakter alfanumerik dan garis bawah (A-z, 0-9, dan _ )
>Nama variabel peka huruf besar/kecil (usia, usia, dan usia adalah tiga variabel yang berbeda)
>Nama variabel tidak dapat berupa salah satu kata kunci Python.
"""
myvar = "Maria"
my_var = "Maria"
_my_var = "Maria"
myVar = "Maria"
MYVAR = "Maria"
myvar2 = "Maria"
print(myvar)
#nama variabel multi kata
myVariableName = "Maria"
MyVariableName = "Maria"
my_variable_name = "Maria"


##assign multiple values
#banyak nilai ke beberapa variabel
x, y, z = "pagi", "siang", "malam"
print(x)
print(y)
print(z)
#satu nilai untuk beberapa variabel
x = y = z = "malam"
print(x)
print(y)
print(z)
#membongkar daftar, yaitu mengestrak nilai menjadi variabel
hari = ["senin", "selasa", "rabu"]
x, y, z = hari
print(x)
print(y)
print(z)


##output variables
#untuk menghasilkan beberapa varibale, pisahkan dengan tanda koma atau (+) 
x = "hari"
y = "ini"
z = "cerah"
print(x, y, z)
print(x + y + z)
#dapat juga menggunakan operator + (untuk angka berfungsi sebagai operator matematika: +)
x = "hari "
y = "ini "
z = "cerah"
print(x + y + z) #karakter spasi sebelum tanda kutip berguna agar kalimat memiliki spasi
#untuk menggabungkan variaibel dengan tipe data berbeda, gunakan tanda koma
x = 5
y = "saya"
print(x, y)


##global variables
#variabel global: dibuat di luar fungsi, bisa dipakai di mana saja
x = "cerah"
def myfunc():
    print("cuaca hari ini " + x)

myfunc()

#variabel lokal: dibuat di dalam fungsi, hanya bisa dipakai di dalam fungsi itu saja
x = "cerah"
def myfunc():
  x = "mendung"
  print("cuaca hari ini " + x)

myfunc()

print("cuaca hari ini " + x)

#kata kunci global > variabel termasuk dalam cakupan global
def myfunc():
  global x
  x = "cerah"

myfunc()

print("cuaca hari ini " + x)

#kata kunci global dapat mengubah nilai variabel di dalam fungsi
x = "cerah"
def myfunc():
  global x
  x = "mendung"

myfunc()

print("cuaca hari ini " + x)