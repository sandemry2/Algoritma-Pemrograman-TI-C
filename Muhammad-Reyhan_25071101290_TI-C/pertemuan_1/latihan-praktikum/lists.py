#lists 
name = ["alif", "maja", "jiha"]
print(name) # return ['alif', 'maja', 'jiha']
print(type(name)) # return <class 'list'>

#accessing elements
print(name[0]) # return alif
print(name[1]) # return maja
print(name[2]) # return jiha

#slicing
print(name[0:2]) # return ['alif', 'maja']
print(name[1:3]) # return ['maja', 'jiha']
print(name[2:3]) # return ['jiha']

#length
print(len(name)) # return 3

#methods
name.append("reyhan") # return ['alif', 'maja', 'jiha', 'reyhan']
print(name)
name.insert(1, "budi") # return ['alif', 'budi', 'maja', 'jiha', 'reyhan']
print(name)
name.remove("maja") # return ['alif', 'budi', 'jiha', 'reyhan']
print(name)
name.pop() # return ['alif', 'budi', 'jiha']
print(name)
name.reverse() # return ['jiha', 'budi', 'alif']
print(name)
name.sort() # return ['alif', 'budi', 'jiha']
print(name)
name.count("alif") # return 1
print(name)
name.index("alif") # return 0
print(name)
name.copy() # return ['alif', 'budi', 'jiha']
print(name)
name.clear() # return []
print(name)

#list comprehension
name = ["alif", "maja", "jiha"]
print([name for name in name]) # return ['alif', 'maja', 'jiha']

#nested list
name = ["alif", "maja", "jiha", ["budi", "siti", "budi"]]
print(name) # return ['alif', 'maja', 'jiha', ['budi', 'siti', 'budi']]
print(name[3][0]) # return budi
print(name[3][1]) # return siti
print(name[3][2]) # return budi

