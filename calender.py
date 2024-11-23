from datetime import datetime

days_of_week = ["Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"]
months_of_year = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

year = input("Enter month and year: ")
year = "1/" + year
year_format = datetime.strptime(year,"%d/%m/%Y")

show_month = months_of_year[year_format.month-1]
show_year = year_format.year
print(f"{show_month} {show_year}")

for i in days_of_week:
    print(i,end="\t")
print("")

first_day_month = year_format.isoweekday()

month = year_format.month
yyear = year_format.year
end = 30
if month in [1,3,5,7,8,10,12]:
    end = 31
elif month ==2:
    if (yyear%400==0)or (year%100!=0 and year % 4 ==0):
        end = 29
    else:
        end = 28
d = 1

for i in range(1,44):
    if i < first_day_month:
        print(" ",end="\t")
    elif d>end:
        print(" ",end="\t")
    else:    
        print(d,end="\t")
        d+=1

    if i % 7 == 0:
        print()
