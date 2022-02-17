# A Python function is a reusable named block of code that performs a task or returns a value.
# Use the def keyword to define a new function. A function consists of function definition and body.
# A function can have zero or more parameters. If a function has one or more parameters, you need to pass the same number of arguments into it.
# A function can perform a job or return a value. Use the return statement to return a value from a function.

def sum(x, y):
    return x + y


total = sum(33, 23)
print(total)


# Default Parameters
def greet(name, message='Hi'):
    return f'{message} {name}'


msg = greet('John')
print(msg)
msg = greet('John', 'Hello')
print(msg)

# Keyword Arguments
# Use the Python keyword arguments to make your function call more readable and obvious,
# especially for functions that accept many arguments.
# All the arguments after the first keyword argument must also be keyword arguments too.


def get_net_price(price, discount):
    return price * (1 - discount)


print(get_net_price(price=100, discount=0.6))

# Python lambda expressions
# Use Python lambda expressions to create anonymous functions, which are the functions without names.
# A lambda expression accepts one or more arguments, contains an expression, and returns the result of that expression.
# Use lambda expressions to pass anonymous functions to a function and return a function from another function.


def get_full_name(firstName, lastName, formatter):
    return formatter(firstName, lastName)


fullName = get_full_name(
    'John',
    'Wick',
    lambda first_name, last_name: f"{first_name} {last_name}"
)

print(fullName)
