'''
    Recursion is a method of programming or coding a problem, in which a function calls itself one or more times 
    in its body. Usually, it is returning the return value of this function call. If a function definition 
    satisfies the condition of recursion, we call this function a recursive function.
'''

# Lets start with a simple example where we will print 0 to 9 using a recursive function


def PrintNumbers(num):
    if num >= 10:  # Termination condition
        return
    else:
        print(num)
        return PrintNumbers(num+1)


if __name__ == '__main__':
    PrintNumbers(0)

'''
    Termination condition: A recursive function has to fulfil an important condition to be used in a program: 
    it has to terminate. A recursive function terminates, if with every recursive call the solution of 
    the problem is downsized and moves towards a base case. A base case is a case, where the problem 
    can be solved without further recursion. A recursion can end up in an infinite loop, 
    if the base case is not met in the calls.

'''
