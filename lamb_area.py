import math

def shape_area(func,*num):
    return func(*num)

circle = lambda r : math.pi * (r**2)
square = lambda x , y : x * y
rectangle = lambda x , y : x * y
triangle = lambda w , h : 0.5 * w * h

circle_area = shape_area(circle, 10)
print(f"Circle area: {circle_area:.2f}")

square_area = shape_area(square, 10)
print(f"Square area: {square_area:.2f}")

rectangle_area = shape_area(rectangle, 10, 20)
print(f"Rectangle area: {rectangle_area:.2f}")

triangle_area = shape_area(triangle, 10, 20)
print(f"Triangle area: {triangle_area:.2f}")