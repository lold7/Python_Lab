from datetime import date , timedelta


months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

time = date.today()

day = [0 ,3 ,7,28,90]

for i ,d in enumerate(day):
    next = timedelta(days=d)
    time_next = time.__add__(next)
    print(f"Vaccine dose {i+1} injected on the {time_next.day} {months[time_next.month - 1]} {time_next.year}")