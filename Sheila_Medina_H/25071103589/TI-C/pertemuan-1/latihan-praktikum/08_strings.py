#1.string + escape
#string dalam Python dikelilingi oleh tanda kutip tunggal atau tanda kutip ganda.

print("Hello")  #ini sama saja dengan
print('Hello')  #ini

#jika kita ingin menampilkan tanda kutip di dalam string, kita bisa menggunakan tanda kutip yang berbeda

print("'Isn't it a beautiful day?'said isabel.")  #menggunakan tanda kutip ganda di luar
print('He said "Hello!"')      #menggunakan tanda kutip tunggal di luar

#atau kita bisa menggunakan karakter escape (\)
print('It\'s a beautiful day')  #menggunakan karakter escape untuk tanda kutip tunggal
print("He said \"Hello!\"")      #menggunakan karakter escape untuk tanda kutip ganda

#2.slice strings
'''kita dapat mengembalikan rentang karakter dengan menggunakan sintaks slice.
Tentukan indeks awal dan indeks akhir, 
dipisahkan oleh titik dua, untuk mengembalikan sebagian dari string.'''

b = "Hello, World!"
print(b[2:5])  #mengambil karakter dari indeks 2 sampai 5 (tidak termasuk indeks 5)

#2.a slice from the start
#Dengan menghilangkan indeks awal, rentang akan dimulai dari karakter pertama:
b = "Hello, World!"
print(b[:5]) #mengambil karakter dari awal sampai indeks 5 (tidak termasuk indeks 5)

#2.bslice to the end
#Ambil karakter dari posisi 2, dan terus sampai ke akhir.
b = "Hello, World!"
print(b[2:]) #mengambil karakter dari indeks 2 sampai akhir string

#2.c negative indexing
#Gunakan indeks negatif untuk memulai pengirisan dari akhir string:
b = "Hello, World!"
print(b[-5:-2]) #mengambil karakter dari indeks -5 sampai -2 (tidak termasuk indeks -2)

#3.Replace and Other String Methods
#beberapa metode string yang umum digunakan di Python. Berikut
''' beberapa replace string adalah sebagai berikut:
1. replace() : Mengganti sebuah string dengan string lainnya
2. upper()	: Mengubah string menjadi huruf besar semua
3. lower()	: Mengubah string menjadi huruf kecil semua
4. strip()	: Menghapus spasi di awal dan di akhir string
5. split()	: Memecah string menjadi beberapa bagian berdasarkan pemisah tertentu
6. join()	: Menggabungkan elemen-elemen dalam sebuah iterable menjadi satu string dengan pemisah tertentu
7. find()	: Mencari posisi pertama dari sebuah substring dalam string
8. format()	: Memformat string dengan menyisipkan nilai-nilai tertentu
'''
#3.a replace()
txt = "I like bananas"
print(txt.replace("bananas", "apples"))  #mengganti "bananas" dengan "apples"

#3.b upper()
txt = "Hello World"
print(txt.upper())  #mengubah semua huruf menjadi huruf besar

#3.c lower()
txt = "Hello World"
print(txt.lower())  #mengubah semua huruf menjadi huruf kecil

#3.d strip()
txt = "   Hello World   "
print(txt.strip())  #menghapus spasi di awal dan akhir string

#3.e split()
txt = "Hello, World"
print(txt.split(","))  #memecah string menjadi list berdasarkan koma

#3.f join()
mylist = ["Hello", "World"]
print(" ".join(mylist))  #menggabungkan elemen list menjadi string dengan spasi sebagai pemisah

#find()
txt = "Hello, World"
print(txt.find("World"))  #mencari posisi pertama dari substring "World"

#3.h format()
txt = "My name is {} and I am {} years old."
print(txt.format("Alice", 30))  #memformat string dengan menyisipkan nilai-nilai tertentu

#4. String Concatenation
a = "Hello"
b = "World"
c = a + " " + b #pakai + untuk menggabungkan dua string dan tambahkan " "
print(c)  #menggabungkan dua string dengan spasi di antara mereka

#5.f-Strings
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  
#menggunakan f-string untuk menyisipkan variabel ke dalam string

#6. Escape Characters (revisi)
#beberapa escape characters lainnya 
print("Line1\nLine2")      #newline
print("Column1\tColumn2")  #tab
print("This is a backslash: \\")  #backslash
print('It\'s a beautiful day!')  #menggunakan karakter escape untuk tanda kutip tunggal
print("C:\\Users\\Alice")   #menggunakan karakter escape untuk backslash ganda
print("She said \"It's okay.\"")  #menggunakan karakter escape untuk tanda kutip ganda dan tunggal
print("First Line\rSecond Line")  #carriage return
print("Hello\bWorld")        #backspace
