#1.Fungsi Python (Functions)
'''Fungsi adalah blok kode yang hanya berjalan saat dipanggil.
Fungsi dapat mengembalikan data sebagai hasilnya.
Fungsi membantu menghindari pengulangan kode.'''

#Dalam Python, sebuah fungsi didefinisikan menggunakan kata kunci `def`, 
# iikuti oleh nama fungsi dan tanda kurung.

def my_function():
  print("Hello from a function")

my_function()  
'''memanggil fungsi dengan cara menuliskan nama fungsi
diikuti tanda kurung'''

#a.the pass statement
'''Jika kita ingin membuat fungsi
    tanpa isi, kita dapat menggunakan pernyataan `pass`
    untuk menghindari kesalahan sintaks.'''
def empty_function():
    pass

#2.the function arguments

#a.Function Arguments
'''Informasi dapat diteruskan ke fungsi sebagai argumen.
Argumen ditentukan setelah nama fungsi, di dalam tanda kurung. 
Kita dapat menambahkan argumen sebanyak yang kita inginkan, 
cukup pisahkan dengan koma.
Contoh berikut memiliki fungsi dengan satu argumen (name). 
Saat fungsi dipanggil, kita meneruskan nama depan, 
yang digunakan di dalam fungsi untuk mencetak nama lengkap.'''

def greet(name): #name adalah parameter
    print("Hello, " + name + "!")
greet("Alice")
greet("Bob") #bob adalah argumen

'''Dari perspektif fungsi
Parameter adalah variabel yang tercantum di dalam tanda kurung pada definisi fungsi.
Argumen adalah nilai sebenarnya yang dikirim ke fungsi saat dipanggil.'''

#b.Multiple Arguments
'''Fungsi dapat memiliki beberapa argumen,
dipisahkan dengan koma.'''

def add(a, b): 
  return a + b   '''ini juga namanya return value 
                    yaitu nilai yang dikembalikan oleh fungsi''''

result = add(5, 3) #memanggil fungsi dengan argumen 5 dan 3
print("The sum is:", result) #menampilkan hasil penjumlahan

#c.Default Arguments
'''Kita dapat menetapkan nilai default untuk argumen fungsi.
Jika argumen tidak diberikan saat pemanggilan fungsi,
nilai default akan digunakan.'''
def greet(name="Guest"):
    print("Hello, " + name + "!")

greet()          # Menggunakan nilai default
greet("Charlie") # Menyediakan argumen


'''Mengapa Menggunakan Fungsi?
Bayangkan kita perlu mengkonversi suhu dari Fahrenheit ke Celsius beberapa kali
 dalam program kita. Tanpa fungsi, 
kita harus menulis kode perhitungan yang sama berulang kali.'''

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

'''Dengan menggunakan fungsi, kita hanya perlu menulis kode konversi sekali.
Kemudian, kita dapat memanggil fungsi tersebut setiap kali 
kita perlu melakukan konversi suhu.
Ini membuat kode kita lebih bersih, lebih mudah dibaca, 
dan lebih mudah untuk diatur.''' #udah capek plis ini udh dari jam 4 sore ngerjainnya ;(
                                  #jam 10 malem masih juga ngerjain :((

#d.Number of Arguments
'''Secara default, sebuah fungsi harus dipanggil dengan jumlah argumen yang tepat.
Jika fungsi kita mengharapkan 2 argumen, kita harus memanggilnya
 dengan tepat 2 argumen.Jika kita mencoba memanggil 
fungsi dengan jumlah argumen yang tidak sesuai, Python akan memberikan error.'''
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")