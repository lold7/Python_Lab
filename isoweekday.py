from datetime import datetime


day = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
time = datetime.today()
time_index = time.weekday()

print(day[time_index])