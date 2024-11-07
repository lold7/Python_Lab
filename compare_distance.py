foot = 3280.84
yard = 1093.61
mile = 0.62
kilo = 1

print("Kilometer\tFoot\t\tYard\t\tMile")
for i in range(1,11):
    print(f"{kilo*i}\t\t{foot*i:,.2f}\t{yard*i:,.2f}\t{mile*i:,.2f}")