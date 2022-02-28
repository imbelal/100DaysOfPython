# Lets implement the factorial in Python using recursive function
# Factorial of 5 is 5*4*3*2*1 = 120

def Factorial(num, result=1):
    if num == 0:
        return result
    else:
        result = result * num
        return Factorial(num-1, result)


if __name__ == '__main__':
    result = Factorial(5)
    print(result)
