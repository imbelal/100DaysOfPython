# If you’ve been working in other programming languages such as Java, C#, or C/C++,
# you know that these languages use semicolons (;) to separate the statements.
# Python, however, uses whitespace and indentation to construct the code structure.
# In Python, a single line comment begins with a hash (#) symbol followed by the comment.
# define main funnction to print out something

def main():
    i = 0
    max = 10

    while (i < max):
        print(i)
        i = i + 1

    # Python uses a newline character to separate statements. It places each statement on one line.
    if (True) and (True) and \
            (True):
        print("Continuation of statements")


# call main function
main()
