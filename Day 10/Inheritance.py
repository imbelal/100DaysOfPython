# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.


# Here Person is a class with properties name, age, gender and a method named printDetails
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def printDetails(self):
        print(f'Name: {self.name} Age: {self.age} gender: {self.gender}')


# Here Student is a class which inherite Person class
# As Student class is a child class of Person class, it has all the properties that Person class has
# Student class also has a extra property cgpa and a method printCgpa
# The __init__() function is called automatically every time the class is being used to create a new object.
# Python has a super() function that will make the child class inherit all the methods and properties from its parent

class Student(Person):
    def __init__(self, name, age, gender, cgpa):
        super().__init__(name, age, gender)
        self.cgpa = cgpa

    def printCgpa(self):
        print(f'cgpa: {self.cgpa}')


# Here Teacher is a class which inherite Person class
# As Teacher class is a child class of Person class, it has all the properties that Person class has
# Teacher class also has a extra property salary and a method printSalary

class Teacher(Person):
    def __init__(self, name, age, gender, salary):
        super().__init__(name, age, gender)
        self.salary = salary

    def printSalary(self):
        print(f'salary: {self.salary}')


# Here we are creating object of both child class and calling their print details method
s1 = Student('Belal', 22, 'male', 3.5)
t1 = Teacher('John', 55, 'male', 65000)

s1.printDetails()  # calling parent method
s1.printCgpa()  # calling own method

t1.printDetails()  # calling parent method
t1.printSalary()  # calling own method
