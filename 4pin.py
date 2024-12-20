count = 0
currect = 3253

while True:
    if count == 4:
        print("You enter pin 4 time")
        break
    pin = int(input("Enter pin: ")) 
    if pin == currect:
        print("Complete")
        break
    else:
        count +=1
    