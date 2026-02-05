# FUNCTION ARGUMENT

def my_function(fname): # fname adalah parameter.
    print(fname + " Ahyaritama")

my_function("Riyanda") # Sedangkan "Riyanda" adalah argumen.

# Output: Riyanda Ahyaritama

# Jumlah argumen harus menyesuaikan dengan jumlah parameter. Tidak boleh
# lebih banyak ataupun lebih sedikit. Tetapi, jika sebuah fungsi memiliki
# parameter opsional, maka jumlah argumen bisa lebih sedikit.

def my_function_optional(name = "friend"):
    print("Hello", name)

my_function_optional()
# Output: Hello friend

my_function_optional("sir")
# Output: Hello sir

# Parameter tersebut akan menggunakan nilai defaultnya jika tidak ada argumen
# yang diberikan. Jika argumen diberikan, maka argumennya akan digunakan