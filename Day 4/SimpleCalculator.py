# A basic calculator to perform addition, subtraction, multiplication and division operator

def add(num1, num2):
    '''This function adds two numbers'''
    return num1 + num2


def subtract(num1, num2):
    '''This function subtracts two numbers'''
    return num1 - num2


def multiply(num1, num2):
    '''This function multiplies two numbers'''
    return num1 * num2


def divide(num1, num2):
    '''This function divides two numbers'''
    return num1 / num2


command = 'y'
while command.lower() == 'y':
    print('Select a operation')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')

    operation = int(input("Enter choice(1/2/3/4): "))
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if(operation == 1):
        print(num1, "+", num2, "=", add(num1, num2))
    elif(operation == 2):
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif(operation == 3):
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif(operation == 4):
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("invalid!!")
    command = input('Do you want to calculate again? (y/n): ')
