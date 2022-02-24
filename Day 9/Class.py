# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# To create a class, use the keyword class:
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary
# to do when the object is being created
# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.
# you can call it whatever you like, but it has to be the first parameter of any function in the class

class Account:
    def __init__(self, name, age, accountNo, balance):
        self.name = name
        self.age = age
        self.accountNo = accountNo
        self.balance = balance

    def showBalance(self):
        print("Name: " + self.name + " Account: " +
              self.accountNo + f" Balance: {self.balance}")

    def transfer(self, toAccount, amount):
        if(self.balance - amount >= 0):
            self.balance -= amount
            toAccount.balance += amount


a1 = Account("John", 36, '001', 500)
a2 = Account("Rock", 36, '001', 200)
a1.transfer(a2, 200)
a1.showBalance()
a2.showBalance()


# Delete Objects
del a1
del a2
