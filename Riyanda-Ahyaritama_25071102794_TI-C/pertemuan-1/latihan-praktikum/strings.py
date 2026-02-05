# STRINGS
# SYNTAX (SINTAKS)

print("Hello") # Hello
print('Hello') # Hello
# Menggunakan Double Quotes ataupun Single Quotes merupakan
# preferensi masing-masing, keduanya benar.
# ============================================================================ #


# QUOTES INSIDE QUOTES

print("Nama saya 'Riyanda Ahyaritama'")     # Nama saya 'Riyanda Ahyaritama'
print('Nama saya "Riyanda Ahyaritama"')     # Nama saya "Riyanda Ahyaritama"
print("Nama saya \"Riyanda Ahyaritama\"")   # Nama saya "Riyanda Ahyaritama"
# Bisa menggunakan Double/Single Quotes di dalam string selama Quote nya
# berbeda dengan pembuka & penutup string atau jika diberi Backslash (\)
# sebelum tanda petik.
# ============================================================================ #


# STRING DENGAN BANYAK BARIS

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# Selain digunakan untuk komentar (banyak digunakan untuk dokumentasi),
# 3 Double/Single Quotes dapat digunakan sebagai string, dan akan dicetak
# baris per baris mengikuti format penulisan aslinya.
# ============================================================================ #


# MENGIRIS STRING

b = "Hello World!"
print(b[2:5]) # llo
# Mengiris string yang dimulai dari index ke-2 hingga ke-(5-1).

b = "Hello, World!"
print(b[:5]) # Hello
# Mengiris string yang dimulai dari index ke-0 hingga ke-(5-1).

b = "Hello, World!"
print(b[2:]) # llo, World!
# Mengiris string yang dimulai dari index ke-2 hingga terakhir.

b = "Hello, World!"
print(b[-5:-2]) # orl
# Mengiris string yang dimulai dari index ke-5 dari belakang hingga ke-(2-1) dari belakang.
# ============================================================================ #


# MODIFIKASI STRING

a = " Hello World! "
print(a.upper())                     # ` HELLO WORLD! `             | Mengubah semua huruf menjadi Upper Case.
print(a.lower())                     # ` hello world! `             | Mengubah semua huruf menjadi Lower Case.
print(a.strip())                     # `Hello World!`               | Menghapus spasi di depan dan belakang.
print(a.replace("World", "Riyanda")) # ` Hello Riyanda! `           | Mengubah huruf/kata.
print(a.split(" "))                  # ['', 'Hello', 'World!', '']  | Mengubah string menjadi list dengan menggunakan pemisah.
# ============================================================================ #


# MENGGABUNGKAN STRING

a = "Hello"
b = "World!"
c = a + b
print(c) # HelloWorld!
c = a + " " + b
print(c) # Hello World!
# ============================================================================ #


# FORMAT STRING

age = 19
txt = f"My name is Riyanda, I am {age}"
print(txt) # My name is Riyanda, I am 19
# ============================================================================ #


# ESCAPE KARAKTER

print("Nama saya \"Riyanda Ahyaritama\"")   # Nama saya "Riyanda Ahyaritama"
# Escape karakter dilakukan dengan cara menambahkan Backslash (`\`) sebelum
# karakter yang ingin di escape.