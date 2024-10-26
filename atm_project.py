def atm_func():  
    while True:
        my_money = int(input("ระบุจำนวนเงินที่ต้องการ: "))
        if my_money in range(100,10000,10):

            b1000 = int(my_money / 1000)
            b1000r = int(my_money % 1000)
            b500 = int(b1000r / 500)
            b500r = int(b1000r % 500)
            b100 = int(b500r / 100)
            b100r = int(b500r % 100)
            b50 = int(b100r / 50)
            b20 = int(b100r / 20)
            print(f"แบงค์พันจำนวน {b1000} ใบ\nแบงค์ห้าร้อยจำนวน {b500} ใบ\nแบงค์ร้อยจำนวน {b100} ใบ\nแบงค์ห้าสิบจำนวน {b50} ใบ\nแบงค์ยี่สิบจำนวน {b20} ใบ\n")
            break
        else:
            print("จำนวนเงินไม่ถูกต้อง กรุณาลองอีกครั้ง")
            
atm_func()
print("                  ")