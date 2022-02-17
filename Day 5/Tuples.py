'''
    A tuple is a collection of objects which ordered and immutable. Tuples are sequences, just like lists.
    The differences between tuples and lists are, the tuples cannot be changed unlike lists and 
    tuples use parentheses, whereas lists use square brackets.
'''

# Tuples are immutable lists.
# Use tuples when you want to define a list that cannot change.

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"

# iteration in touples
for item in tup1:
    print(item)

# The empty tuple is written as two parentheses containing nothing
tup1 = ()

# Converts a list into tuple.
list = [1, 2, 3, 4]
print(list)
tupleFromList = tuple(list)
print(tupleFromList)
