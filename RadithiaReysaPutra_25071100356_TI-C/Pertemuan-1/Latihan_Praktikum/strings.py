a = "Hello World!"
print(a,type(a))

#multiline strings
a = """Kegagalan adalah
kesempatan untuk
memulai lagi."""
print(a,type(a))

#looping dalam string

for a in "mangga": #Lakukan perulangan melalui huruf-huruf dalam mangga
  print(a)

#string lenght
a = "Hello, World!" #akan menghitung panjang string
print(len(a))

#check string
txt = "The best things in life are free!" #cek apakah kata free ada dalam string
print("free" in txt)

#slicing string
b = "Hello, World!"
print(b[1:5]) #akan memotong string dan menampilkan karakter dari posisi 1 hingga 5

#modifikasi string
a = "Hello, World!"
print(a.upper()) #mengubah string menjadi huruf besar semua

a = "Hello, World!"
print(a.lower()) #mengubah string menjadi huruf kecil semua

a = " Hello, World! "
print(a.strip()) #menghapus spasi di awal dan di akhir string

a = "Hello, World!"
print(a.replace("H", "J")) #mengubah huruf dalam string

a = "Hello, World!"
print(a.split(",")) #membagi string menjadi substring jika menemukan kemunculan pemisah tersebut

#menggabungkan string
a = "Hello"
b = "World"
c = a + b
print(c) # gunakan kutip dua dan spasi didalamnya agar teks tersebut tidak menyatu

#format string
age = 36
txt = f"My name is John, I am {age}" #gunakan "f" untuk menggabungkan antara integer dengan string
print(txt)

#escape character
txt = 'It\'s alright.'#(\')digunakan untuk memberi kutip didalam string
print(txt) 

txt = "This will insert one \\ (backslash)." #(\\)digunakan untuk memberi garis miring dalam string
print(txt) 

txt = "Hello\nWorld!" #untuk new line
print(txt) 

txt = "Hello\rWorld!"#akan menampilkan kata setelah return
print(txt) 

txt = "Hello\tWorld!" #memberikan jarak tab pada string
print(txt) 

txt = "Hello \bWorld!" #menghapus 1karakter sebelum (\b)
print(txt) 

txt = "\110\145\154\154\157" #(\000)akna menampilkan octal value
print(txt) 

txt = "\x48\x65\x6c\x6c\x6f" #akan menampilkan hex value
print(txt) 

#string methods
text = "python"
print(text.capitalize())  # Huruf pertama jadi besar
text = "PyThOn"
print(text.casefold())  # Mengubah ke huruf kecil (lebih agresif dari lower)
text = "Python"
print(text.center(10, "-"))  # Teks di tengah, sisanya diisi "-"
text = "banana"
print(text.count("a"))  # Menghitung jumlah huruf 'a'
text = "python"
print(text.encode())  # Mengubah string ke bytes
text = "file.txt"
print(text.endswith(".txt"))  # Cek apakah string diakhiri ".txt"
text = "P\tython"
print(text.expandtabs(4))  # Mengganti tab dengan spasi
text = "hello world"
print(text.find("world"))  # Posisi kata "world"
name = "Andi"
print("Halo {}".format(name))  # Menyisipkan nilai ke string
data = {"nama": "Budi"}
print("Halo {nama}".format_map(data))  # Format pakai dictionary
text = "python"
print(text.index("t"))  # Posisi huruf 't' (error jika tidak ada)
text = "Python123"
print(text.isalnum())  # Cek huruf dan angka saja
text = "Python"
print(text.isalpha())  # Cek hanya huruf
text = "Hello"
print(text.isascii())  # Cek karakter ASCII
text = "123"
print(text.isdecimal())  # Cek angka desimal
text = "²"
print(text.isdigit())  # Cek digit (lebih luas dari decimal)
text = "var_1"
print(text.isidentifier())  # Cek valid sebagai nama variabel
text = "python"
print(text.islower())  # Cek semua huruf kecil
text = "123"
print(text.isnumeric())  # Cek angka (paling luas)
text = "Hello\n"
print(text.isprintable())  # Cek karakter bisa dicetak
text = "   "
print(text.isspace())  # Cek hanya spasi
text = "Hello World"
print(text.istitle())  # Cek format judul
text = "PYTHON"
print(text.isupper())  # Cek semua huruf besar
data = ["Python", "Java", "C++"]
print(", ".join(data))  # Menggabungkan list jadi string
text = "Python"
print(text.ljust(10, "-"))  # Rata kiri
text = "PYTHON"
print(text.lower())  # Ubah ke huruf kecil
text = "   Python"
print(text.lstrip())  # Hapus spasi kiri
table = str.maketrans("aeiou", "12345")
text = "python"
print(text.translate(table))  # Ganti karakter
text = "email@gmail.com"
print(text.partition("@"))  # Pisah jadi 3 bagian
text = "I like Java"
print(text.replace("Java", "Python"))  # Ganti kata
text = "banana"
print(text.rfind("a"))  # Posisi terakhir "a"
text = "banana"
print(text.rindex("a"))  # Posisi terakhir "a" (error jika tidak ada)
text = "Python"
print(text.rjust(10, "-"))  # Rata kanan
text = "a,b,c"
print(text.rsplit(","))  # Split dari kanan
text = "Python   "
print(text.rstrip())  # Hapus spasi kanan
text = "Python is fun"
print(text.split())  # Pisah berdasarkan spasi
text = "Hello\nWorld"
print(text.splitlines())  # Pisah per baris
text = "hello.py"
print(text.startswith("hello"))  # Cek awalan
text = "  Python  "
print(text.strip())  # Hapus spasi kiri & kanan
text = "PyThOn"
print(text.swapcase())  # Tukar huruf besar-kecil
text = "belajar python"
print(text.title())  # Awal kata jadi huruf besar
text = "python"
print(text.upper())  # Ubah ke huruf besar
text = "42"
print(text.zfill(5))  # Isi nol di depan