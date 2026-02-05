# casting string to int
x = int("10")
print(x)
print(type(x))

# casting int to string
y = str(10)
print(y)
print(type(y))

# casting float to int
z = int(10.5)
print(z)
print(type(z))

# casting int to float
a = float(10)
print(a)
print(type(a))

# casting bool to int
b = int(True)
print(b)
print(type(b))

# casting int to bool
c = bool(10)
print(c)
print(type(c))

# casting list to tuple
d = tuple([1, 2, 3])
print(d)
print(type(d))

# casting tuple to list
e = list((1, 2, 3))
print(e)
print(type(e))

# casting dict to tuple
f = tuple({"name": "John", "age": 30})
print(f)
print(type(f))

# casting tuple to dict
g = dict({"name": "John", "age": 30})
print(g)
print(type(g))

# casting set to tuple
h = tuple({1, 2, 3})
print(h)
print(type(h))

# casting tuple to set
i = set((1, 2, 3))
print(i)
print(type(i))

# casting frozenset to tuple
j = tuple(frozenset({1, 2, 3}))
print(j)
print(type(j))

# casting tuple to frozenset
k = frozenset((1, 2, 3))
print(k)
print(type(k))

# casting binary to int
l = int("1010", 2)
print(l)
print(type(l))

# casting octal to int
m = int("12", 8)
print(m)
print(type(m))

# casting hexadecimal to int
n = int("1A", 16)
print(n)
print(type(n))

# casting int to binary
o = bin(10)
print(o)
print(type(o))

# casting int to octal
p = oct(10)
print(p)
print(type(p))

# casting int to hexadecimal
q = hex(10)
print(q)
print(type(q))

# casting complex to int
r = int(10 + 2j)
print(r)
print(type(r))

# casting complex to float
s = float(10 + 2j)
print(s)
print(type(s))

# casting complex to complex
t = complex(10 + 2j)
print(t)
print(type(t))
