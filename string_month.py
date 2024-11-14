from datetime import datetime

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


date_input = input("Enter date(D/M/Y): ")

time = datetime.strptime(date_input,"%d/%m/%Y")

d = time.day
m = months[time.month - 1]
y = time.year

print(f"{d} {m} {y}")