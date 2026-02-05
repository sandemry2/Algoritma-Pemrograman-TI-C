##python data types
#tipe data bawaan python
"""
Jenis Teks:	str
Jenis Numerik: int, , floatcomplex
Jenis Urutan: list, , tuplerange
Jenis Pemetaan: dict
Jenis Tetap: set, frozenset
Tipe Boolean: bool
Jenis biner: bytes, , bytearraymemoryview
Tidak ada Jenis: NoneType
"""

#mengecek tipe data
x = "abcd"
print(type(x))

#mengatur tipe data
"""
x = "Hello World"   >str: 
x = 20	>int	
x = 20.5	>float	
x = 1j	complex	
x = ["pagi", "siang", "malam"]	>list	
x = ("pagi", "siang", "malam")	>tuple	
x = range(6)	>range	
x = {"name" : "Maria", "age" : 19}	>dict	
x = {"pagi", "siang", "malam"}	>set	
x = frozenset({"pagi", "siang", "malam"})	>frozenset	
x = True	>bool	
x = b"Hello"	>bytes	
x = bytearray(5)	>bytearray	
x = memoryview(bytes(5))	>memoryview	
x = None	>NoneType	
"""
