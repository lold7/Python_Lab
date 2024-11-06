num_list = []
for i in range(1,4):
    i = int(input(f"Enter number({i}): "))
    num_list.append(i)
max = num_list[0]
min = num_list[0]
for j in range(len(num_list)):
    if max < num_list[j]:
        max = num_list[j]

for j in range(len(num_list)):
    if min > num_list[j]:
        min = num_list[j]


print(f"max: {max} min: {min}")