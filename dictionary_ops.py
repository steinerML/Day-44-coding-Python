#Dictionary Operations

dict1 = {'H' : 'Hello', 'G' : 'Good', 'J': 'Jeep', 'K': 'Kelvin'}

#Acces element
print(dict1['H'])

#Acces all keys
print(dict1.keys())

#Access all values
print(dict1.values())

#Add element
dict1['X'] = 'Xgamer'
print(dict1)

#Delete Elements
del dict1['H']
print(dict1)

#Clear the dictionary but keeps the object <dict>
inp_dict = {"A":"Python","B":"Java","C":"Fortan","D":"Javascript"}
inp_dict.clear()
print("\nElements after deletion operation:")
print(inp_dict)

#Another way of deleting. now with pop()
dict1.pop('K')
print(dict1)

#Popitem removes last added element.
dict1.popitem()
print(dict1)

#Sort dictionary by keys alphabetically
bykeys = sorted(list(dict1.keys()))
print(bykeys)
#Sort dictionary by values alphabetically
byvalues = sorted(list(dict1.values()))
print(byvalues)

#Dictionary comprehension
a = {i : i**3 for i in (1,2,3,4,5,6,7,8,9,10)}
print(a)

