# Use Python try...except statement to handle exceptions gracefully.
# Use specific exception in the except block as much as possible.
# Use the except Exception statement to catch other exceptions.

try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = num1 / num2  # if num2 = 0 then it will occur an error
    print(f'Result: {result}')
except:
    print('Please try again!')

# Catching specific exceptions

try:
    num1 = 6
    num2 = 0
    result = num1 / num2  # as num2 = 0 then it will occur an error
    print(f'Result: {result}')
except ZeroDivisionError as error:
    print('Divisor should not be zero!')

# Handling multiple exceptions
try:
    num1 = 6
    num2 = 0
    result = num1 / num2  # as num2 = 0 then it will occur an error
    print(f'Result: {result}')
except ZeroDivisionError as error:
    print('Divisor should not be zero!')
except ValueError as error:
    print('Error! Please enter a number.')

# try-finally Clause
try:
    num1 = 6
    num2 = 0
    result = num1 / num2  # as num2 = 0 then it will occur an error
    print(f'Result: {result}')
except:
    print('Error! something went wrong.')
finally:
    print('final step')
