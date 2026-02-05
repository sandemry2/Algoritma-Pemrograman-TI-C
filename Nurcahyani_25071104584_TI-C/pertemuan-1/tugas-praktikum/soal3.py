#menentukan kategori kelulusan
nilai = int(input("Masukkan nilai ujian: "))
if 100 >= nilai >= 60:
    print("Lulus")
elif 60 > nilai >= 0:
    print ("Tidak Lulus")
else:
    print ("Nilai tidak valid")