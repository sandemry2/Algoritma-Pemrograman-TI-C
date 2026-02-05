#Aritmatika
x = 15
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#Assigments
"""
=	   x = 5	      x = 5	
+=	   x += 3	      x = x + 3	
-=	   x -= 3	      x = x - 3	
*=	   x *= 3	      x = x * 3	
/=	   x /= 3	      x = x / 3	
%=	   x %= 3	      x = x % 3	
//=	x //= 3	      x = x // 3	
**=	x **= 3	      x = x ** 3	
&=	   x &= 3	      x = x & 3	
|=	   x |= 3	      x = x | 3	
^=	   x ^= 3	      x = x ^ 3	
>>=	x >>= 3	      x = x >> 3	
<<=	x <<= 3	      x = x << 3	
"""

#Comparison
"""
== 	Equal	                     x == y	
!= 	Not equal	               x != y	
>  	Greater than	            x > y	
<  	Less than	               x < y	
>= 	Greater than or equal to	x >= y	
<= 	Less than or equal to	   x <= y
"""
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#CHAINING COMPARISON
x = 5
print(1 < x < 10)
print(1 < x and x < 10)
print('\n')


#LOGICAL OPERATORS
"""
and 	   Returns True if both statements are true	                  x < 5 and  x < 10	
or	      Returns True if one of the statements is true	            x < 5 or x < 4	
not	   Reverse the result, returns False if the result is true	   not(x < 5 and x < 10)"""


# IDENTITIY OPERATORS
"""
is 	   Returns True if both variables are the same object	         x is y	
is not	Returns True if both variables are not the same object      x is not y
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)  # returns True because z is the same object as x
print(x is y)  # returns False because x is not the same object as y, even if they have the same content
print(x == y)  # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
print('\n')

print(x is not z) # returns False because z is the same object as x
print(x is not y) # returns True because x is not the same object as y, even if they have the same content
print(x != y)     # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
print('\n')

# Difference Between is and ==
#is - Checks if both variables point to the same object in memory
#== - Checks if the values of both variables are equal


# MEMBERSHIP
"""
in 	   Returns True if a sequence with the                x in y	
         specified value is present in the object	         
not in	Returns True if a sequence with the                x not in y
         specified value is not present in the object	
         """
#Check if "banana" is present in a list:
fruit = ["apple", "banana", "cherry"]
print("banana" in fruit)
print ("watermelon" not in fruit)

# Membership di string
text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)


# BITWISE
# Digunakan untuk membandingkan (binary) numbers
"""
& 	   AND	                  Sets each bit to 1 if both bits are 1	            x & y	
|	   OR	                     Sets each bit to 1 if one of two bits is 1	      x | y	
^	   XOR	                  Sets each bit to 1 if only one of two bits is 1	   x ^ y	
~	   NOT	                  Inverts all the bits	                              ~x	
<<	   Zero fill left shift	   Shift left by pushing zeros in from the right      x << 2
                              and let the leftmost bits fall off		
>>	   Signed right shift	   Shift right by pushing copies of the leftmost      x >> 2
                              bit in from the left, and let the rightmost 
                              bits fall off   
"""
# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 2 = 0010
print(6 & 3)

# The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 7 = 0111
print(6 | 3)

# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 5 = 0101
print(6 ^ 3)

print (~3)