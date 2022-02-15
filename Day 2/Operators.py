# Python has six comparison operators: less than (<), less than or equal to (<=), greater than (>),
#  greater than or equal to (>=), equal to (==), and not equal to (!=).

x = 5
y = 8

if(x <= 8):
    print(x)

# Logical Operators
# Python has three logical operators: and, or, not

if(x >= 5 and y <= 10):
    print("It's logical!!")

# Ternary operator: value_if_true if condition else value_if_false
age = input('Enter your age:')
ticketPrice = 20 if int(age) >= 18 else 0
print(ticketPrice)
