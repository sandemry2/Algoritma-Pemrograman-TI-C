#Python Variabel
x = str(8)    # x akan menjadi '8'
y = int(8)    # y akan menjadi 8
z = float(8)  # z akan menjadi 8.0

#case sensitive, kedua nama variabel tersebut berbeda
a = 7
A = 8
print(a,A)

#Variable Names
#legal
myname = "Radith"
my_Name = "Radith"
_my_name = "Radith"
myName = "Radith"
MYNAME = "Radith"
myname2 = "Radith"

#ilegal
# 2myname = "Radith" #angka tidak boleh diawal
# my-name = "Radith" #tidak boleh ada tanda (-)
# my name = "Radith" #tidak boleh ada spasi/jarak

#Multiple Variables
x , y , z = "Rudi","Beni","Sukadi"
print(x)
print(y)
print(z)

#collection
buah = "mangga", "sirsak", "apel"
x,y,z = buah
print(x)
print(y)
print(z)

#output variabel
x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #koma membuat kalimat menjadi berjarak
print(x + y + z) # (+) membuat menjadi kalimat namun tanpa jarak

a = 5
b = "budi"
print (a+b) # (+) tidak dapat menggabungkan antara string dengan angka
print (a, b) # (,) koma dapat menggabungkan antara string dengan angka