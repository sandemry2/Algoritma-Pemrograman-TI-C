print("Hello World")
print('hello world')

#multiline strings
print("""Hello World""") # return Hello World
print('''hello world''') # return hello world
print("""
dua lima satu lima sepuluh
tiga empat lima
""") # return 
#dua lima satu lima sepuluh
#tiga empat lima

#string concatenation
print("Hello" + " World") # return Hello World
print("Hello" + " " + "World") # return Hello World
print("Hello" + " " + "World" + "!") # return Hello World!

#string repetition
print("Hello" * 3) # return HelloHelloHello
print("Hello" * 0) # return 
print("Hello" * -1) # return 

#string indexing
print("Hello"[0]) # return H
print("Hello"[1]) # return e
print("Hello"[2]) # return l
print("Hello"[3]) # return l
print("Hello"[4]) # return o

#string slicing 
print("Hello"[0:2]) # return He
print("Hello"[1:3]) # return el
print("Hello"[2:4]) # return ll
print("Hello"[3:5]) # return lo
print("Hello"[4:5]) # return o

#string length
print(len("Hello")) # return 5

#string method
print("uppercase".upper()) # return uppercase to UPPERCASE
print("lowercase".lower()) # return lowercase to LOWERCASE
print("   hello world   ".strip()) # return    hello world    to hello world
print("replace123".replace("123", "python")) # return replace123 to replacepython
print("hello world".split(" ")) # return hello world to ["hello", "world"]
print("capitalize".capitalize()) # return capitalize to Capitalize
print("title case".title()) # return title case to Title Case
print("swapcase".swapcase()) # return swapcase to SWAPCASE
print("find".find("d")) # return find to 3
print("index".index("d")) # return index to 2
print("counttt".count("t")) # return count to 3
print("hello world".startswith("world")) # return False
print("hello world".endswith("world")) # return True
print("hello world".isalnum()) # return False
print("hello world".isalpha()) # return False
print("hello world".isdigit()) # return False
print("hello world".islower()) # return True
print("hello world".isupper()) # return False
print("hello world".istitle()) # return False
print("hello world".isspace()) # return False



