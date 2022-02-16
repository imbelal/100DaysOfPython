'''
    The BMI is a measure of some's weight taking into account their height. e.g. 
    If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
    The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
'''


from math import exp


height = input("Enter your height in meter: ")
weight = input("Enter your wieght in kg: ")
# The Python ** operator is used to raise a number in Python to the power of an exponent.
bmi = float(weight) / float(height) ** 2
bmi = round(bmi, 2)
print(f"BMI: {bmi}")
