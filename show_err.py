try:
    x = 1/0
    print(x)
except ValueError as err:
    print(err)