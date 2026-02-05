# --- BAB: MATCH CASE ---
# Pastikan menggunakan Python versi 3.10 ke atas

status = 200

match status:
    case 200:
        print("OK - Berhasil")
    case 404:
        print("Not Found - Tidak Ditemukan")
    case 500:
        print("Server Error")
    case _:
        print("Status tidak dikenali") # Default case