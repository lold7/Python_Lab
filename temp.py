import random

def check(temperature):
    if temperature < 36.5:
        raise Exception ("Too low temperature")
    elif temperature > 37.8:
        raise Exception ("Too high temperature")
    else:
        return temperature
    
temperature = random.uniform(36,38)
try:
    checking = check(temperature)
except Exception as err:
    print(err)
else:
    print(checking)