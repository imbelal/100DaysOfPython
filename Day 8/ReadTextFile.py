# Use the open() function with the 'r' mode to open a text file for reading.
# Use the read(), readline(), or readlines() method to read a text file.
# Always close a file after completing reading it using the close() method or the with statement.
# Use the encoding='utf-8' to read the UTF-8 text file.

with open('ZenOfPython.txt') as f:
    contents = f.read()
    print(contents)

# The following example uses the readlines() method to read the text file and returns the file contents
# as a list of strings:

lines = []
with open('ZenOfPython.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    print(f'line {count}: {line}')

# The following example shows how to use the readline() to read the text file line by line:
with open('ZenOfPython.txt') as f:
    line = f.readline()
    while line:
        line = f.readline()
        print(line)

# A more concise way to read a text file line by line
with open('ZenOfPython.txt') as f:
    for line in f:
        print(line)

# To open a UTF-8 text file, you need to pass the encoding='utf-8' to the open() function to instruct
# it to expect UTF-8 characters from the file.
with open('MyGoldenBengal.txt', encoding='utf8') as f:
    for line in f:
        print(line.strip())
