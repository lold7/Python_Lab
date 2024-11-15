from datetime import date,timedelta

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

time_1 = date.today()

print(f"Pruduced on the {time_1.day} {months[time_1.month-1]} {time_1.year}")

next120 = timedelta(days=120)
print(f"Product has a shelf life of 120 days")


time_2 = time_1.__add__(next120)

print(f"Product expires on the {time_2.day} {months[time_2.month-1]} {time_2.year}")