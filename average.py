sum = 0
for i in range(1,6):
    i = int(input(f"Enter number({i}): "))
    sum += i

average = sum/len(range(1,6))

print(f"Sum: {sum} Average: {average}")