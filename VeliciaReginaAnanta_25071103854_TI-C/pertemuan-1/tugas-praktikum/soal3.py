# MENENTUKAN KATEGORI KELULUSAN BERDASARKAN NILAI UJIAN

score = int(input('Masukkan nilai ujian (0-100): '))

if (60 <= score <= 100.):
    print('Lulus')
elif (0 <= score < 60):
    print('Tidak Lulus')
else:
    print("Nilai Tidak Valid")