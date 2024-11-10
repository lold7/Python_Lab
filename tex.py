
salary = int(input("Fill your salary: "))

income = salary * 12

spend = income * (40/100)
if spend > 60000:
    spend = 60000

discount = 30000

income -= (spend+discount)

if income in range(0,150000):
    rate = 0/100

elif income in range(150001,300001):
    rate = 5/100

elif income in range(300001,500001):
    rate = 10/100

elif income in range(500001,750001):
    rate = 15/100

elif income in range(750001,1000001):
    rate = 20/100

elif income in range(1000001,2000001):
    rate = 25/100

elif income in range(2000001,5000001):
    rate = 30/100

elif income > 5000000:
    rate = 35/100

tex = (income-150000) * rate

print(f"Tex: {tex}")