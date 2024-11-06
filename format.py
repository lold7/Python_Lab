a = "{:,}".format(1234)
print(f"product: {a}")

b = format(4324252324,",")
print(f"money: {b}")

c = "{:.3f}".format(234.23434923)
print(c)

day = format(3 , "0>2")
month = "{:0>2}".format(7)

print(f"{day} / {month} / 2024")