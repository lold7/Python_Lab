def item(**data):
    first = True
    for i in data:

        if not first:
            print(", ",end="")

        print(f"{i}: {data[i]}" ,end=" ")
        first = False


item(name = "Iphone" , price = 40000,storage = "256GB")
