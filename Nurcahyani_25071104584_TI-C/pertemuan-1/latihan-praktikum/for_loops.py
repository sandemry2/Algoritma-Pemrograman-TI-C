#menjabarkan each item list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("====================")
#menjabarkan kata secara vertikal
for x in "banana":
  print(x)

print("====================")
#break statement ketika mencapai kondisi tertentu
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print("====================") 
#countinue statement dengan hasil banana tidak masuk hitungan
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("====================")
#range function dengan indeks
for x in range(6):
  print(x)

print("====================")
#else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

print("====================")
#nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)