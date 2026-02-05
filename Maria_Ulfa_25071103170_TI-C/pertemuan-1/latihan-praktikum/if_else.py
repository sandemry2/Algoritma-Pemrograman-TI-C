##python if
#kondisi python dan pernyataan if
"""
Sama dengan: a == b
Tidak Sama: a != b
Kurang dari: < b
Kurang dari atau sama dengan: a <= b
Lebih besar dari: a > b
Lebih besar dari atau sama dengan: a >= b
"""

a = 33
b = 200
if b > a:
  print("b is greater than a")

#mengevaluasi kondisi menghasilkan ekspresi true/false
number = 15
if number > 0:
  print("The number is positive")

#beberapa pernyataan di if block
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

#menggunakan variabel dalam kondisi
is_logged_in = True
if is_logged_in:
  print("Welcome back!")


##python elif
#Kata kunci elif adalah cara Python mengatakan 
#"jika kondisi sebelumnya tidak benar, maka Cobalah kondisi ini".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#beberapa pernyataan elif
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

#cara kerja elif (mengevaluasi kondisi dari atas ke bawah)
age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")

#kapan menggunakan elif (elif digunakan ketika memiliki beberapa ketentuan yang saling eksklusif untuk diperiksa)
day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")


##python else
#kata kunci else
#Pernyataan else dijalankan ketika kondisi if (dan kondisi elif apa pun) dievaluasi ke False.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#else tanpa elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#cara kerja lain
number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#rantai if-elif-else lengkap
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")


##shorthand if
#pernyataan satu : if
a = 5
b = 2
if a > b: print("a is greater than b")

#satu baris / yang mencetak nilai: if else
a = 2
b = 330
print("A") if a > b else print("B")

#beberapa kondisi dalam satu jalur
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#contoh praktis (menemukan maksimum dua angka)
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)


##logical operators
#operator dan
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#operator atau
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#operator bukan
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#menggabungkan beberapa operator
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

#menggunakan tanda kurung untuk kejelasan
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")


##nested if
#pernyataan jika bersarang
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#beberapa tingkat bersarang
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

#bersarang jika vs operator
temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")


##pass statement
#pernyataan lulus
a = 33
b = 200

if b > a:
  pass

#lulus dalam pengembangan
age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

#lulus vs komentar
score = 85

if score > 90:
  pass # This is excellent
print("Score processed")

#lulus dengan beberapa kondisi
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")




