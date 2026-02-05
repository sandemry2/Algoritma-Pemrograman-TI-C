#match case
perintah = input("Masukkan perintah (mulai/berhenti/tunda): ").lower()

match perintah:
    case "mulai":
        print("Sistem sedang berjalan...")
    case "berhenti":
        print("Sistem telah dihentikan.")
    case "tunda":
        print("Sistem ditunda.")
    case _:
        print("Perintah tidak dikenali.")


#match case with if
perintah = input("Masukkan perintah (mulai/berhenti/tunda): ").lower()

match perintah:
    case "mulai" if perintah == "mulai":
        print("Sistem sedang berjalan...")
    case "berhenti" if perintah == "berhenti":
        print("Sistem telah dihentikan.")
    case "tunda" if perintah == "tunda":
        print("Sistem ditunda.")
    case _:
        print("Perintah tidak dikenali.")
