
a = 5
b = 10

print(a == b) # return False, karena a tidak sama dengan b
print(a != b) # return True, karena a tidak sama dengan b
print(a > b) # return False, karena a lebih kecil dari b
print(a < b) # return True, karena a lebih kecil dari b
print(a >= b) # return False, karena a lebih kecil dari b
print(a <= b) # return True, karena a lebih kecil dari b

# logical operators
print(a and b) # return 10, karena a dan b adalah integer
print(a or b) # return 5, karena a dan b adalah integer
print(not a) # return False, karena a adalah integer

# boolean operations
print(a & b) # return 0, karena a dan b adalah integer
print(a | b) # return 15, karena a dan b adalah integer
print(a ^ b) # return 15, karena a dan b adalah integer
print(~a) # return -6, karena a adalah integer
print(a << b) # return 327680, karena a adalah integer
print(a >> b) # return 0, karena a lebih kecil dari b

# boolean functions
print(bool(a)) # return True, karena a adalah integer
print(bool(b)) # return True, karena b adalah integer
print(bool(0)) # return False, karena 0 adalah integer
print(bool(1)) # return True, karena 1 adalah integer
print(bool("hello")) # return True, karena "hello" adalah string
print(bool("")) # return False, karena "" adalah string
print(bool([1, 2, 3])) # return True, karena [1, 2, 3] adalah list
print(bool([])) # return False, karena [] adalah list
print(bool((1, 2, 3))) # return True, karena (1, 2, 3) adalah tuple
print(bool(())) # return False, karena () adalah tuple
print(bool({1: "hello", 2: "world"})) # return True, karena {1: "hello", 2: "world"} adalah dictionary
print(bool({})) # return False, karena {} adalah dictionary
print(bool({1, 2, 3})) # return True, karena {1, 2, 3} adalah set
print(bool(set())) # return False, karena set() adalah set
