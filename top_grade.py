score_list = []

for i in range(1,7):
    score = int(input(f"Student {i}: "))
    score_list.append(score)

top = max(score_list)

for i in range(len(score_list)):
    if score_list[i] >= top - 10:
        print(f"Student {i+1} Grade A")
    elif score_list[i] >= top - 20:
        print(f"Student {i+1} Grade B")
    elif score_list[i] >= top - 30:
        print(f"Student {i+1} Grade C")
    elif score_list[i] >= top - 40:
        print(f"Student {i+1} Grade D")
    else :
        print(f"Student {i+1} Grade F")