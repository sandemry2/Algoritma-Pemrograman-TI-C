#python if
#Multiple Statements di dalam if block
nilai = 85
if nilai >= 75:
    print("Lulus")          # Pernyataan pertama
    print("Nilai bagus")    # Pernyataan kedua
    print("Selamat!")       # Pernyataan ketiga

#python elif
nilai = 86
if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai C")
elif nilai >= 60:
    print("Nilai D")
elif nilai <60:
    print("Nilai E")

#menggabungkan if , elif , dan else
nilai = 20
if nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
elif nilai >= 70:
    print("Grade C")
elif nilai >= 60:
    print("Grade D")
else:
    print("Grade E")

#nested if
umur = 20
punya_sim = True

if umur >= 17:
    if punya_sim:
        print("Boleh mengemudi")      # if di dalam if
    else:
        print("Umur cukup, tapi belum punya SIM")
else:
    print("Belum cukup umur")
