try:
    value = int(input("Enter number: "))
    if value not in range(1,101):
        raise Exception("Number must be in range 1-100 only")
    print(f"Value is: {value}")
except Exception as err:
    type = err.__class__
    if type == ValueError:
        print("Number must be whole number")
    else:
        print(err)
    