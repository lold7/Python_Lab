from datetime import date,timedelta

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

today = date.today()
print(f"Today is the {today}")

appoint = int(input("Appointment day: "))
next_app = timedelta(days=appoint)

appoint_day = today.__add__(next_app)
week = appoint_day.isoweekday()

if week == 6:
    next2 = timedelta(days=2)
    appoint_day = appoint_day.__add__(next2)
    print(f"Appointment day is: {appoint_day.day} {months[appoint_day.month-1]} {appoint_day.year}" )

elif week == 7:
    next1 = timedelta(days=1)
    appoint_day = appoint_day.__add__(next1)
    print(f"Appointment day is: {appoint_day.day} {months[appoint_day.month-1]} {appoint_day.year}" )

else:
    print(f"Appointment day is: {appoint_day.day} {months[appoint_day.month-1]} {appoint_day.year}" )
