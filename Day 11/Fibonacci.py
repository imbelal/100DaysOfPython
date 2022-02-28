# Lets implement the fibonacci series in Python using recursive function
# The Fibonacci numbers are the numbers of the following sequence of integer values
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

def Fibonacci(num):
    if num == 0:
        return num
    elif num == 1:
        return num
    else:
        return Fibonacci(num - 1) + Fibonacci(num - 2)


if __name__ == '__main__':
    num = 0
    while num < 10:  # we will find first 10 numbers from fibonacci series
        result = Fibonacci(num)
        print(result)
        num += 1
