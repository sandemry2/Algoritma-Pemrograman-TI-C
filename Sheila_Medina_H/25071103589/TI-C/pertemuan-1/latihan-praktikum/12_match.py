#Match 
'''Pernyataan `match` digunakan untuk melakukan tindakan berbeda 
berdasarkan kondisi yang berbeda.
Alih-alih menulis banyak pernyataan `if..else`, 
kita dapat menggunakan pernyataan `match`.
Pernyataan `match` memilih salah satu dari banyak blok kode untuk dieksekusi.'''

# Contoh Penggunaan Struktur Match...Case dalam Python
# 1️.Struktur Dasar

color = "red"
match color:
    case "red":
        print("Warna adalah Merah")  # dijalankan karena color adalah "red"
    case "blue":
        print("Warna adalah Biru")
    case "green":
        print("Warna adalah Hijau")


# 2️.Match dengan Default Case
'''Gunakan karakter garis bawah _ sebagai nilai kasus terakhir 
jika Anda ingin blok kode dieksekusi ketika tidak ada kecocokan lain'''

color = "yellow"
match color:
    case "red":
        print("Warna adalah Merah")
    case "blue":
        print("Warna adalah Biru")
    case _:
        print("Warna tidak dikenal")  # dijalankan karena tidak ada kecocokan lain