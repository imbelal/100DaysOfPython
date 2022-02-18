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

# Union sets using union() method
s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

s = s1.union(s2)
print(s)

# Union sets using the | operator
x = s1 | s2
print(x)

# Python set union operator only supports set while union() method supports one or more iterables

# Python set intersection
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1.intersection(s2)
print(s)

# Using Python set intersection (&) operator to intersect two or more sets
x = s1 & s2
print(x)

# The set intersection operator only allows sets, while the set intersection() method can accept any iterables, like strings, lists, and dictionaries.


# Use Python Set difference() method to find the difference between sets
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1.difference(s2)
print(s)

# Using Python set difference operator (-) to find the difference between sets
x = s1 - s2
print(x)

# The set difference() method can accept one or more iterables (e.g., strings, lists, dictionaries)
# while the set difference operator (-) only allows sets.

# symmetric difference of sets
# The symmetric difference of two sets is a set of elements that are in either set,
# but not in their intersection.
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1.symmetric_difference(s2)
print(s)
# Using the symmetric difference operator(^) to find the symmetric difference of sets
x = s1 ^ s2
print(x)

# The symmetric_difference() method accepts one or more iterables that can be strings, lists, or dictionaries.
# However, the symmetric difference operator (^) only applies to sets. If you use it with the iterables which aren’t sets, you’ll get an error.


# Python issubset() method
# Suppose that you have two sets A and B. The set A is a subset of the set B if all elements of A are also elements of B.
# Then, the set B is a superset of the set A
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}
print(scores.issubset(numbers))
# Besides using the issubset() method, you can use subset operators (<=) to check if a set is a subset of another set
print(scores <= numbers)

# The proper subset operator (<) check if the set_a is a proper subset of the set_b:
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = scores < numbers
print(result)  # True

result = numbers < numbers
print(result)  # False


# Python issuperset method
# Suppose that you have two sets: A and B. Set A is a superset of set B if all elements of set B are elements of set A.
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = numbers.issuperset(scores)
print(result)
# The >= operator determines if a set is a superset of another set:
print(numbers >= scores)

# To check if a set is a proper superset of another set, you use the > operator:
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = numbers > scores
print(result)  # True

result = numbers > numbers
print(result)  # False

# Python isdisjoint() method
# Two sets are disjoint when they have no elements in common. In other words,
# two disjoint sets are sets whose intersection is an empty set.
odd_numbers = {1, 3, 5}
even_numbers = {2, 4, 6}

result = odd_numbers.isdisjoint(even_numbers)
print(result)
