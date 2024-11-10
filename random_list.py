import random

my_list = []

for i in range(1,11):
    i = random.randint(1,100)
    my_list.append(i)

sum = sum(my_list)
max = max(my_list)
min = min(my_list)

print("All value:", *my_list)
print(f"Sum: {sum}\nMax: {max}\nMin: {min}")