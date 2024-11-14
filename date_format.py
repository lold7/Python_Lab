from datetime import date

time = date.today()

time_format = time.strftime("%d--%m--%Y")

print(time_format)