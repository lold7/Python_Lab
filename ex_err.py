try:
    x = 1/0
    print(x)
except Exception as err:
    type = err.__class__
    print(type)
    print(err)