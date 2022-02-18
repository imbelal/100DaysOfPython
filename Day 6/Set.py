# A Python set is an unordered list of immutable elements.
# Elements in a set are unordered.
# Elements in a set are unique. A set doesn’t allow duplicate elements.
# Elements in a set cannot be changed. For example, they can be numbers, strings, and
# tuples, but cannot be lists or dictionaries.
# To define a set in Python, you use the curly brace {}

skills = {'Python programming', 'Databases', 'Software design'}

# To define an empty set, you cannot use the curly braces like this
empty_set = {}  # because it defines an empty dictionary
# you need to use the built-in set() function
empty_set = set()

# You can pass an iterable to the set() function to create a set.
skills = set(['Problem solving', 'Critical Thinking'])
print(skills)

# If an iterable has duplicate elements, the set() function will remove them.
characters = set('letter')
print(characters)

# Getting sizes of a set
print(len(set({1, 2, 3, 4})))

# To check if a set contains an element, you use the in operator
if 1 in {1, 2, 3, 4}:
    print('we found 1 in the set')

# Adding elements to a set
numbers = {1, 2, 3, 4}
numbers.add(5)
print(numbers)
# To remove an element from a set, you use the remove() method
numbers.remove(5)
print(numbers)

# To remove and return an element from a set, you use the pop() method.
print(numbers.pop())

# To remove all elements from a set, you use the clear() method:
numbers.clear()
print(numbers)

# Frozen a set
numbers = {1, 2, 3, 4}
frozenset(numbers)
# After that, if you attempt to modify elements of the set, you’ll get an error:
# numbers.add(5) # you will get error because the set is already frozen

# iterate through the set
skills = {'Problem solving', 'Software design', 'Python programming'}

for index, skill in enumerate(skills):
    print(f"{index}.{skill}")
