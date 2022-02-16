from math import exp


height = input("Enter your height in meter: ")
weight = input("Enter your wieght in kg: ")
# The Python ** operator is used to raise a number in Python to the power of an exponent.
bmi = float(weight) / float(height) ** 2
bmi = round(bmi, 2)
print(f"BMI: {bmi}")
