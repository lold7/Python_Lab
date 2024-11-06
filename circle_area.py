import math

radius = float(input("Enter radius: "))

area = (4/3) *math.pi*(radius**3)

result = format(area,",.2f")

print(f"Radius: {radius}\nArea : {result}")