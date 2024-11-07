sum_weight = 0
people_amount = 0
print("Enter x to end of operation")
while sum_weight <= 500:
    weight = (input("Enter people weight: "))
    if weight == "x" or weight == "X":
        break
    people_amount +=1
    sum_weight += int(weight)
    if sum_weight > 500:
        sum_weight = sum_weight - int(weight)
        break
    
print(f"{people_amount} people\nSum weight: {sum_weight}")