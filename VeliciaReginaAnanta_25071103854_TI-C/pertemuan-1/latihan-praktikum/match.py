# MATCH STATEMENT
# memilih satu dari banyak blok kode untuk di eksekusi

"""
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
"""

day = 3
match day:
   case 1:
      print("Monday")
   case 2:
      print("Tuesday")
   case 3:
      print("Wednesday")
   case 4:
      print("Thursday")
   case 5:
      print("Friday")
   case 6:
      print("Saturday")
   case 7:
      print("Sunday")
   case _:
      print("Not Match") #Default value

# COMBINE VALUE
# menggunakan Pipe karakter (|) sebagai operator untuk mengecek lebih dari satu nilai yang sesuai dalam satu case
hari = 4
match hari:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

# Menambahkan IF untuk pengecekan tambahan
Bulan = 5
Hari = 4
match Hari:
  case 1 | 2 | 3 | 4 | 5 if Bulan == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if Bulan == 5:
    print("A weekday in May")
  case _:
    print("No match")