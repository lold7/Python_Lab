import random

def dices():
    a = random.randint(1,6)
    b = random.randint(1,6)
    return a,b

throw = dices()
print(throw)