def number():
    
    try:
        num = int(input("Fill number 1-4: "))
        num
        if num > 4 or num < 1:
            raise Exception ("Please fill number 1 - 4 only")
    
    except Exception as err:
        print(err)

number()