width = int(input("Width >> "))
height = int(input("Height >> "))

zoom = int(input("Zoom: "))
zoom /= 100

width *= zoom
height *= zoom

print(f"The result : {width} x {height}")