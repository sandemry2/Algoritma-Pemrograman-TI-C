# FUNGSI MENGHITUNG DUA BILANGAN8
a = int(input('Angka pertama: '))
b = int(input('Angka kedua: '))

def hitung(a,b):
    tambah = a+b
    kurang = a-b
    return tambah, kurang
penjumlahan, pengurangan = hitung(a,b)

print('Hasil penjumlahan: ',penjumlahan)
print('Hasl pengurangan: ',pengurangan)