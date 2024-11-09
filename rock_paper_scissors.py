print("1 >> Rock\n2 >> Paper\n3 >> Scissors")

while True:
    try:
        try:
            p1 = int(input("Player 1: "))
            p2 = int(input("Player 2: "))
        except ValueError as error:
            print("Please Enter number 1,2,3 only.Try again")
            continue
        
        if p1 > 3 or p2 > 3 or p1 < 1 or p2 < 1:
            raise Exception("Please enter a number (1, 2, or 3) only. Try again.")
        
        if p1 == 1:
            if p2 == 2:
                print("Player 2 win")
                break
            elif p2 == 3:
                print("Player 1 win")
                break
            else:
                print("It's a tie! Try again.")
    
        if p1 == 2:
            if p2 == 1:
                print("Player 1 win")
                break
            elif p2 == 3:
                print("Player 2 win")
                break
            else:
                print("It's a tie! Try again.")
    
        if p1 == 3:
            if p2 == 2:
                print("Player 1 win")
                break
            elif p2 == 1:
                print("Player 2 win")
                break
            else:
                print("It's a tie! Try again.")  
    except Exception as err:
        print(err)