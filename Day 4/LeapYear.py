# Leap year checker

def isLeapYear(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is Leap Year")
    else:
        print(f"{year} is not Leap Year")


while True:
    year = int(input("Enter year: "))
    isLeapYear(year)
