# --- BAB: FUNCTION ARGUMENTS ---

# 1. Default Parameter
def salam(negara="Indonesia"):
    print("Saya dari " + negara)

salam("Jepang")
salam() # Akan pakai default (Indonesia)

# 2. Arbitrary Arguments (*args)
# Jika tidak tahu berapa banyak argumen yang masuk (jadi Tuple)
def fungsi_banyak_arg(*anak):
    print("Anak termuda adalah " + anak[2])

fungsi_banyak_arg("Emil", "Tobias", "Linus")

# 3. Keyword Arguments (kwargs)
def fungsi_kunci(anak3, anak2, anak1):
    print("Anak termuda adalah " + anak3)

fungsi_kunci(anak1="Emil", anak2="Tobias", anak3="Linus")

# 4. Arbitrary Keyword Arguments (**kwargs)
# Jika argumen berupa key-value tak terbatas (jadi Dictionary)
def fungsi_lengkap(**orang):
    print("Nama belakangnya adalah " + orang["lname"])

fungsi_lengkap(fname="Tobias", lname="Refsnes")