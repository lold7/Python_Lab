def product_list(brand , *type):
    print(f"{brand}",end=" ")
    if len(type) > 1:
        s = "Products: "
    else:
        s = "Products: "
    s += ", ".join(type)
    print(s)


product_list("Toyota","Sedan","SUV","Hatchback","Convertible")