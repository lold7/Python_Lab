from datetime import datetime,timedelta

dt = datetime.today()

date_inp = input("Day of Post(Day/Month/Year): ")
post_time = datetime.strptime(date_inp,"%d/%m/%Y")
delta = dt - post_time
delta = delta.days
post_time = post_time.strftime("%d/%m/%Y")

dt = dt.strftime("%d/%m/%Y")
print(f"Time of you post: {post_time}")
print(f"Current time: {dt}")


year = delta // 365
year_remain = delta % 365
month = year_remain // 30
day = year_remain % 30

print(f"{year} Year === {month} Month === {day} Day")
