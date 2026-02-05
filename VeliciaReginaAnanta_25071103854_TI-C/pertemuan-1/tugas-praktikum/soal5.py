# FUNGSI MENGHITUNG DUA BILANGAN

a = int(input('Angka pertama: '))
b = int(input('Angka kedua: '))

def hitung(a, b):
    tambah = a+b
    kurang = a-b
    return tambah, kurang

penjumlahan, pengurangan = hitung(a,b)

print(f'Hasil penjumlahan = {penjumlahan}')
print(f'Hasl pengurangan = {pengurangan}')
