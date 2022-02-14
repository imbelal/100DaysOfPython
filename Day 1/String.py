message = 'This is a string in Python'
message = "This is also a string"

# If a string contains a single quote, you should place it in double-quotes like this:
message = "It's a string"

# And when a string contains double quotes, you can use the single quotes:
message = '"Beautiful is better than ugly.". Said Tim Peters'

# To escape the quotes, you use the backslash (\). For example:
message = 'It\'s also a valid string'

# To span a string multiple lines, you use triple-quotes “””…””” or ”’…”’. For example:
help_message = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''

print(help_message)

# Concatenating Python strings
greeting = 'Good ' 'Morning!'
print(greeting)

# To concatenate two string variables, you use the operator +:
greeting = 'Good '
time = 'Afternoon'

greeting = greeting + time + '!'
print(greeting)


# Since a string is a sequence of characters, you can access its elements using an index.
# The first character in the string has an index of zero.
str = "Python String"
print(str[0])  # P
print(str[1])  # y

# If you use a negative index, Python returns the character starting from the end of the string. For example:
str = "Python String"
print(str[-1])  # g
print(str[-2])  # n

# To get the length of a string, you use the len() function. For example:
str = "Python String"
str_len = len(str)
print(str_len)


# Slicing allows you to get a substring from a string. For example:
str = "Python String"
print(str[0:2])


# Python strings are immutable
