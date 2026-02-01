nama ='Chelsea' 
nim = 25071103316
kelas = 'TI-C' 


print('Halo saya', nama,'saya di kelas', kelas,"dengan nim",nim)

print('Halo saya '+nama+'')

fruits = ['Orange', 'Apple', 'Banana']
x, y, z = fruits =  ['Orange', 'Apple', 'Banana']
print(x)
print (y)
print(z)

print(x, y, z)

score = 85
attendance = 95
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