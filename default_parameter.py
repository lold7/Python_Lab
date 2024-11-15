def total(quantity,price,vat=7):
    return(quantity * price *(1+(vat/100)))

a = total(10 , 100)
b = total(5 , 500 , 7.5)

print(f"{a:,.0f} {b:,.0f}")