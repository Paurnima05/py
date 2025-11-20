dict = {"red": "apple", "yellow": 2, "orange": 3, "green": 4, "blue": 5}

# to print value
for value in dict.values():
    print("value :", value)

# to print key
for key in dict:
    print(key)

# to print both key & value
for key, value in dict.items():
    print(key, ":", value)

# to calculate length
length = len(dict)
print("Length of dictionary is", length)

# to delete key
del dict['red']
print(dict)

# to add key
dict['pink'] = 6
print(dict)

# to modify value
dict['orange'] = 9
print(dict)

# to check whether the key is present or not
print('purple' in dict)
