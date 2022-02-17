# A list is an ordered collection of items.
# Python uses the square brackets ([]) to indicate a list.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# The first element has an index 0.
print(list[0])

# Use a negative index to access a list element from the end of a list. The last element has an index -1
print(list[-1])

# Use list[index] = new_value to modify an element from a list.
list[0] = 10
print(list[0])

# Use append() to add a new element to the end of a list.
list.append(11)
print(list)

# Use insert() to add a new element at a position in a list.
list.insert(2, 11)
print(list)

# Use pop() to remove an element from a list and return that element.
list.pop()
print(list)

# Use remove() to remove an element from a list.
list.remove(11)
print(list)

# List concatenation
print([1, 2, 3] + [4, 5, 6])

# A list can contains other lists.
coordinates = [[0, 0], [100, 100], [200, 200]]
print(coordinates)

# interation in list
for x in coordinates:
    print(x)

# use len() to get length of list
print(len(list))

# use max() to get max value of a list
print(max([1, 2, 3]))

# use min() to get min value of a list
print(min([1, 2, 3]))

# use sorted() to get min value of a list
randomList = [3, 4, 2, 1]
randomList.sort()
print(randomList)

# use reverse() to get min value of a list
randomList.reverse()
print(randomList)
