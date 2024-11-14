from datetime import date,timedelta

time = date.today()

next90 = timedelta(days=90)
next240 = timedelta(days=240)
ago = timedelta(days=-50)

a = time.__add__(next90)
b = time.__add__(next240)
c = time.__add__(ago)

print(f"{a}  {b}  {c}")