# values() ==> get all values from dict

dict1 = {
    'name' : 'Rishi',
    'age'  : 25,
    'isMarried' : False
}

print(dict1.values())

# 2. keys()  ==> get all keys from dict.
print(dict1.keys())

# 3. items()  ==> return all key : value pair as tuples
print(dict1.items())

# 4. get('key')  ==> return the value according to key
print(dict1.get('name'))

# 5. update(newDict) ==>
dict1.update({'marks' : [2,4,2]})
print(dict1)