import random

year = random.randint(1000,2024)

def leap_year(year):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        print(f"{year} is Leap Year")
    else: 
        print(f"{year} is not Leap Year")


x = leap_year(year)
