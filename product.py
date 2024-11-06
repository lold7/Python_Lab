quantity = int(input("Enter quantity: "))
price = int(input("Enter price: "))

total = (quantity * price) - (quantity * price)*(10/100)
print(f"Total price is {total}")

while True:
    pay = int(input("Enter payment: "))
    if pay > total:
        break
    else:
        print("money not enough")
change = pay - total

print(f"Change is {change}")