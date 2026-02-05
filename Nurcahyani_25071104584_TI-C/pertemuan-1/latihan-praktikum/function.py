# Keyword DEF
def my_function():
  print("Hello from a function")

# Fungsi dijalankan saat dipanggil dengan namanya beserta parameter jika ada
my_function()
my_function()

# Return Value
# Saat fungsi mencapai Return Value, eksekusi dihentikan dan return value dikirim

# A function that returns a value:
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

# Using the return value directly:
def get_greeting():
  return "Hello from a function"

print(get_greeting())

# Fungsi dapat memiliki lebih dari 1 return value
a = 4
b = 2
def bagiKali():
  bagi = 4/2
  kali = 4*2
  return bagi, kali
pembagian, perkalian = bagiKali()
print(pembagian)
print(perkalian)


# PASS statement
# Fungsi tidak boleh kosong. Jika inngin membuat sebuah fungsu tanpa kode, gunakan PASS statement
def my_function():
  pass