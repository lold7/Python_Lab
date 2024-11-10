car_price = int(input("Car price: "))

down_price = int(input("Down(%): "))
down_price /= 100
down = car_price*down_price

month = int(input("Month: "))

interest = eval(input("Interest: "))
interest /= 100
interest /= 12

finance = car_price - down

total_int = finance * interest * month

installment = (finance + total_int) / month

print(f"Installment per month: {installment}")