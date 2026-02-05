#STRING SEDERHANA
print("Hello")

#implementasi ke variable
a = "Hello"
print(a)

#menggunakan array, hasilnya akan berdasarkan indeks yang diinginkan
a = "Hello, World!"
print(a[1])

#menghitung length
a = "Hello, World!"
print(len(a))

#SLICING
nama = 'nurcahyani'
print(nama[0:3])     
print(nama[2:])      
print(nama[:4])      
print(nama[:])       
print(nama[-3:])     
print(nama[-5:-3])   

# ESCAPE SEQUENCE
# menambahkan karakter yang ilegal di string
# bisa menggunakan backslash (\)
txt = "We are the so-called \"Vikings\" from the north."
judul = 'Python "Programming"'
judul2 = 'python \'programing\''
print(txt)
print(judul2)

# MODIFY 
kalimat = (' Haloo, umurku 12 tahun ' )
print(kalimat.upper())              # upper
print(kalimat.lower())              # lower
print(kalimat.title())              
print(kalimat.strip())              # remove whitespace left and right
print(kalimat.rstrip())
print(kalimat.split(","))           # return list between text 
print(kalimat.find('tahun'))
print(kalimat.replace('u', 'OO'))    # ganti string dengan string lain
print('umur' in kalimat)
print("tahun" not in kalimat)