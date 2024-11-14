from datetime import date

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

time = date.today()

month_word = months[time.month-1]

print(f"Today is {time.day} {month_word} {time.year}")