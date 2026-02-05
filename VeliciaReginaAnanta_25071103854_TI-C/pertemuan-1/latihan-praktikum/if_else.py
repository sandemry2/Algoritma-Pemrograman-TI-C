# IF STATEMENT
# if mengevaluasi sebuah kondisi (True or False)
# jika True, kode blok dijalankan, jika False, kode blok dilewatkan
num = 5
if (num < 10):
   print ("Angka kurang dari 10")
print('\n')

# bisa dibuat beberapa statement dalam blok, dengan indentation yang sama
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
print('\n')

# Mengunakan variabel
username = True
if username:
   print('Masukkan password')
print('\n')


# ELIF
# elif memungkinkan untuk memeriksa beberapa ekspresi dan mengeksekusi blok kode setelah salah satu kondisi bernilai True
score = 75
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
print ('\n')


# ELSE
# dieksekusi saat if dan elif mengevaluasi False
# else dapat dipakai tanpa adanya elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
print('\n')


# SHORT HAND IF
# jika  hanya memiliki satu pernyataan untuk dieksekusi, Anda dapat meletakkannya pada baris yang sama dengan if
b = 5
c = 2
if a > b: print("b is greater than c")

x= 10
y = 20
bigger = x if x > b else b
print("Bigger is", bigger)
print('\n')

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
print ('\n')

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)
print ('\n')

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
print('\n')

# LOGICAL OPERATOR
temperature = 25
is_raining = False
is_weekend = True
if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")
print ('\n')

age = 25
is_student = False
has_discount_code = True
if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")
print ('\n')

username = "Tobias"
password = "secret123"
is_verified = True
if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")


# NESTED LOOP
age = 25
has_license = True
if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")
print('\n')

score = 85
attendance = 90
submitted = True
if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")
print('\n')

username = "Emil"
password = "python123"
is_active = True
if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")


# PASS
# if loop tidak boleh kosong, tapi jika diperlukan for ;oop tanpa isi, tambahkan PASS 
a = 33
b = 200
if b > a:
  pass