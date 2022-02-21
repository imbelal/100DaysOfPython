# Use the open() function with the w or a mode to open a text file for appending.
# Always close the file after completing writing using the close() method or use the with statement when opening the file.
# Use write() and writelines() methods to write to a text file.
# Pass the encoding='utf-8' to the open() function to write UTF-8 characters into a file.

with open('WriteMe.txt', 'w') as f:
    f.write('WriteMe')

# The following example shows how to use the write() function to write a list of texts to a text file
# If the WriteMe.txt file doesn’t exist, the open() function will create a new file.
lines = ['Write me', 'How to write text files in Python']
with open('WriteMe.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

# The following shows how to write a list of text strings using writelines() method to a text file:
with open('WriteMe.txt', 'w') as f:
    f.writelines(lines)

# If you treat each element of the list as a line, you need to concatenate it with the newline character like this:
with open('WriteMe.txt', 'w') as f:
    f.write('\n'.join(lines))

# Appending text files
more_lines = ['', 'Append text files', 'The End']
with open('WriteMe.txt', 'a') as f:
    f.writelines('\n'.join(more_lines))

# To open a file and write UTF-8 characters to a file, you need to pass the encoding='utf-8' parameter to the open() function.

quote = 'আমার সোনার বাংলা'

with open('quotes.txt', 'w', encoding='utf-8') as f:
    f.write(quote)
