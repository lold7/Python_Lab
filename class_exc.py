import random

data = [0 ,1, "2.3" , 4.5 , 10]

try:
    r = random.choice(data)
    x = int(r)
    y = 10 // x
    z = data[r]

except Exception as err:
    type = err.__class__
    print(type)

finally:
    print(r)