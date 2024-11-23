from datetime import datetime ,timedelta

time = datetime.today()


input_men = input("Enter last menstrual: ")

last_mens = datetime.strptime(input_men,'%d/%m/%Y')

print(f"Last menstrual: {last_mens.strftime('%Y/%m/%d')}")
print(f"Today is: {time.strftime('%Y/%m/%d')}")


day = time - last_mens
day = day.days

month = day//30
num_day = day%30

print(f"{month} Month {num_day} Day")

d280 = timedelta(days = 280)
birth_day = last_mens.__add__(d280)
print(f"Birth Day is: {birth_day.strftime("%Y/%m/%d")}")