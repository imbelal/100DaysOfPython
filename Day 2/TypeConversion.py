# To get an input from users, you use the input() function.
value = input('Enter a value:')
print(value)

# However, the input() function returns a string, not an integer.
# To convert a string to a number, you use the int() function.
# More precisely, the int() function converts a string to an integer.
price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

net_price = int(price) * int(tax) / 100
print(f'The net price is ${net_price}')

# float(str) – convert a string to a floating-point number.
print(float("5.5"))
# bool(val) – convert a value to a boolean value, either True or False.
print(bool("12"))
# str(val) – return the string representation of a value.
print(str(1234))
