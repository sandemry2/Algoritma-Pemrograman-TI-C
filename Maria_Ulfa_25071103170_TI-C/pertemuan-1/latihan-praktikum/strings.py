##python strings
#string dikelilingi tanda kutip
print("Hello")
print('Hello')

#kutipan di dalam kutipan
print("nama saya 'Maria Ulfa'")
print('nama saya "Maria Ulfa"')

#menetapkan string ke variabel
x = "Hai"
print (x)

#string multiline menggunakan 3 tanda kutip(tunggal/ganda)
x = """saya suka makan ayam
saya suka makan ikan
saya suka makan daging"""
print(x)

#string array
x = "Hello world!"
print(x[6])

#mengulang karakter dalam string dengan loop. for
for x in "sayang":
    print(x)

# mencari panjang string menggunakan: len()
x = "sayang"
print(len(x))

#memeriksa apakah suatu karakter/frasa ada dalam string
y = "saya suka makan ayam"
print("makan" in y)

#cetak hanya jika ada kata "makan"
y = "saya suka makan ayam"
if "makan" in y:
    print("ya, kata 'makan' ada")

#memeriksa jika karalter/frasa tidak ada dalam string
y = "saya suka makan ayam"
print("makan" not in y)

#cetak hanya jika tidak ada kata "makan"
y = "saya suka ayam"
if "makan" not in y:
    print("tidak, kata 'makan' tidak ada")


##slicing strings
#mengembalikan rentang karakter dengann sintaks irisan
b = "selamat, malam!"
print(b[0:8])

#irisan dari awal (karakter dari awal sampai ke posisi 6)
b = "selamat, malam!"
print(b[:6])

#irisan sampai akhir (karakter dari posisi 6 sampai akhir)
b = "selamat, malam!"
print(b[6:])

#pengindeksan negatif
b = "selamat, malam!"
print(b[-4:-1])


##modify strings
#mengembalikan string dalam huruf besar gunakan: upper()
a = "selamat, malam!"
print(a.upper())

#mengembalikan string dalam huruf kecil gunakan: lower()
a = "selamat malam!"
print(a.lower())

#menghapus spasi kosong gunakan: strip()
a = " selamat, malam! "
print(a.strip())

#mengganti string menggunakn: replace()
a = "selamat malam!"
print(a.replace("L", "M"))

#memisahkan string gunakan: split()
a = "selamat, malam!"
print(a.split(","))


##concatenation strings
#untuk menggabungkan dua string gunakan: operator +
a = "selamat"
b = "malam"
c = a + b
print(c)

#jika ingin menambahkan spasi
a = "selamat"
b = "malam"
c = a + " " + b
print(c)


##format strings
#angka dan string tidak dapat digabungkan
#untuk menggabungkan keduanya gunakan: f-string
umur = 19
y = f"saya Maria Ulfa, umur saya {umur}"
print(y)

#placeholder dan pengubah
umur = 19
y = f"saya Maria Ulfa, {umur} tahun umur saya"
print(y)

#menyertakan pengubah untuk memformat nilai gunakan: .2f
harga = 59
x = f"harganya adalah {harga:.2f} rupiah"
print(x)

#melakukan operasi matematika di placeholder, dan mengembalikan hasilnya
x = f"harganya adalah {15 * 4000} rupiah"
print(x)


##escape characters
#untuk menyisipkan karakter ilegau are so \"fucking\" l dalam string, gunakan karakter escape: \
x = "We are the so-called \"Vikings\" from the north."
print(x)


##string methods
#metode string pada python
"""
capitalize() → Mengubah karakter pertama menjadi huruf besar
casefold() → Mengubah seluruh string menjadi huruf kecil (lebih kuat dari lower)
center() → Mengembalikan string yang diposisikan di tengah dengan lebar tertentu
count() → Menghitung berapa kali suatu nilai muncul dalam string
encode() → Mengembalikan versi string yang telah dikodekan
endswith() → Mengembalikan True jika string diakhiri dengan nilai tertentu
expandtabs() → Mengatur ukuran spasi untuk karakter tab dalam string
find() → Mencari nilai tertentu dalam string dan mengembalikan posisi ditemukannya
format() → Memformat nilai tertentu ke dalam string
format_map() → Memformat nilai dalam string menggunakan mapping/dictionary
index() → Mencari nilai dalam string dan mengembalikan posisinya (error jika tidak ditemukan)
isalnum() → Mengembalikan True jika semua karakter berupa huruf atau angka
isalpha() → Mengembalikan True jika semua karakter adalah huruf
isascii() → Mengembalikan True jika semua karakter termasuk karakter ASCII
isdecimal() → Mengembalikan True jika semua karakter adalah angka desimal
isdigit() → Mengembalikan True jika semua karakter adalah digit
isidentifier() → Mengembalikan True jika string merupakan nama identifier yang valid
islower() → Mengembalikan True jika semua karakter huruf kecil
isnumeric() → Mengembalikan True jika semua karakter berupa numerik
isprintable() → Mengembalikan True jika semua karakter dapat dicetak
isspace() → Mengembalikan True jika semua karakter adalah spasi
istitle() → Mengembalikan True jika format string seperti judu
isupper() → Mengembalikan True jika semua karakter huruf besar
join() → Menggabungkan elemen iterable menjadi satu string
ljust() → Mengembalikan string rata kiri dengan lebar tertentu
lower() → Mengubah string menjadi huruf kecil
lstrip() → Menghapus spasi di bagian kiri string
maketrans() → Membuat tabel terjemahan untuk digunakan pada translate()
partition() → Membagi string menjadi tiga bagian berdasarkan pemisah
replace() → Mengganti nilai tertentu dengan nilai lain dalam string
rfind() → Mencari nilai dari kanan dan mengembalikan posisi terakhir ditemukan
rindex() → Seperti rfind() tetapi error jika tidak ditemukan
rjust() → Mengembalikan string rata kanan dengan lebar tertentu
rpartition() → Membagi string dari kanan menjadi tiga bagia
rsplit() → Memecah string dari kanan berdasarkan pemisah
rstrip() → Menghapus spasi di bagian kanan string
split() → Memecah string menjadi list berdasarkan pemisa
splitlines() → Memecah string berdasarkan baris baru
startswith() → Mengembalikan True jika string diawali dengan nilai tertentu
strip() → Menghapus spasi di awal dan akhir string
swapcase() → Menukar huruf kecil menjadi besar dan sebaliknya
title() → Mengubah huruf pertama tiap kata menjadi kapital
translate() → Menerjemahkan string menggunakan tabel dari maketrans()
upper() → Mengubah string menjadi huruf besar
zfill() → Menambahkan angka 0 di depan string hingga panjang tertentu
"""
