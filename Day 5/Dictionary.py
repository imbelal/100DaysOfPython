# A Python dictionary is a collection of key-value pairs where each key is associated with a value.
# A value in the key-value pair can be a number, a string, a list, a tuple, or even another dictionary.
# In fact, you can use a value of any valid type in Python as the value in the key-value pair.
# A key in the key-value pair must be immutable. In other words, the key cannot be changed,
# for example, a number, a string, a tuple, etc.

# The following example defines an empty dictionary
empty_dict = {}

# To find the type of a dictionary, you use the type() function as follows:
print(type(empty_dict))

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

print(person)

# To access a value associated with a key, you place the key inside square brackets:
print(person['favorite_colors'])

# We can also use get() method to get the value of a key
print(person.get('first_name'))

# We can assign new value as follows:
person['first_name'] = 'Rock'
print(person['first_name'])

# Removing key-value pairs
del person['active']
print(person)

# Iteration
for key, val in person.items():
    print(f'key: {key}, value: {val}')

# Get only keys
print(person.keys())

# Get only values
print(person.values())
