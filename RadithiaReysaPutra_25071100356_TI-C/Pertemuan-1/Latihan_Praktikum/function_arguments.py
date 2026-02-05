#positional argument
def bio(nama, umur):          # nama dan umur adalah parameter
    print("Nama:", nama)
    print("Umur:", umur)
bio("Andi", 20)               # "Andi" → nama, 20 → umur (urutan penting)

def my_function(name): # ini parameter
  print("Hello", name)
my_function("Emil") # "Emil" adalah argumen

#default argument
def bio(nama="Tamu"):
    print("Halo", nama)

bio("Andi")    # Output: Halo Andi
bio()          # Output: Halo Tamu

#keyword argument
def bio(nama, umur):
    print("Nama:", nama)
    print("Umur:", umur)

bio(umur=20, nama="Budi")      # argumen dipanggil berdasarkan nama parameter

#Arbitrary Arguments (*args)
def jumlahkan(*angka):         # *args menampung banyak argumen
    print(angka)               # disimpan sebagai tuple

jumlahkan(1, 2, 3, 4)          # bisa kirim argumen sebanyak apa pun
jumlahkan()                    # Output: ()  → tuple kosong

#Arbitrary Keyword Arguments (**kwargs)
def biodata(**data):           # **kwargs menampung argumen berbentuk key=value
    print(data)                # disimpan sebagai dictionary

biodata(nama="Dina", umur=22, kota="Jakarta")
biodata()                      # Output: {}  → dictionary kosong

#kombinasi argument
def info(nama, *hobi, kota="Bandung"):
    print("Nama:", nama)
    print("Hobi:", hobi)
    print("Kota:", kota)

info("Eka", "Membaca", "Menulis")   # positional, *args, dan default argument

