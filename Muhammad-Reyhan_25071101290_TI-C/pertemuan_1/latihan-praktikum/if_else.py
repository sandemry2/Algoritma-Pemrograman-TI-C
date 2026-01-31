#if else

nilai = 85
kehadiran = 0.8

if nilai >= 80:
    if kehadiran >= 0.75:
        hasil = "Lulus dengan Pujian (A)"
    else:
        hasil = "Lulus dengan Syarat Kehadiran (B)"
elif nilai >= 60:
    if kehadiran >= 0.75:
        hasil = "Lulus (B)"
    else:
        hasil = "Lulus (C)"
elif nilai >= 40:
    hasil = "Remedial (D)"
else:
    hasil = "Tidak Lulus (E)"

print(f"Status Mahasiswa: {hasil}")


