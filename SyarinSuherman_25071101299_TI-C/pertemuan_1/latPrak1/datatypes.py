# --- BAB: DATA TYPES ---

# Mengetahui tipe data
x = 5
print(type(x)) # <class 'int'>

# 1. Text Type
data_str = "Ini String"

# 2. Numeric Types
data_int = 20
data_float = 20.5

# 3. Sequence Types
data_list = ["Apel", "Jeruk", "Mangga"] # Bisa diubah (Mutable)
data_tuple = ("Apel", "Jeruk", "Mangga") # Tidak bisa diubah (Immutable)
data_range = range(6)

# 4. Mapping Type
data_dict = {"nama": "Budi", "umur": 20} # Key: Value pair

# 5. Set Types
data_set = {"Apel", "Jeruk", "Apel"} # Unik, tidak berurutan

print("List:", data_list)
print("Dictionary:", data_dict)