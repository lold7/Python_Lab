from datetime import date

time_1 = date.today()
time_2 = date(2024 , 1 ,1)

dif_time = time_1 - time_2 

day = dif_time.days

month = day // 30
days = day % 30

print(f"{month} Months {days} Days")