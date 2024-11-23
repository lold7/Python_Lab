from datetime import date

constellation = ("mice","bison","tiger","rabbit","big snake","small snake","horse","goat","monkey","chicken","dog","pig")

year = int(input("Enter year: "))

num_con = (year +5) % 12

your_con = constellation[num_con]
print(f"Your constellation: {your_con}")

num_bad = num_con +6

if num_bad > 12:
    num_bad = num_bad - 12
    bad_year = constellation[num_bad]
else:
    bad_year = constellation[num_bad]

print(f"Bad year is {bad_year}")

year_list = []
for x in range(2500,date.today().year + 543):
    n = (x+5)%12
    if bad_year == constellation[n]:
        year_list.append(x)

print("Year: ",end=" ")  
for i in year_list:
    print(i,end=" ")
