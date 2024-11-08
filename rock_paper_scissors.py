print("1 >> Rock\n2 >> Paper\n3 >> Scissors")

while True:
    p1 = int(input("Player 1: "))
    p2 = int(input("Player 2: "))

    if p1 == 1:
        if p2 == 2:
            print("Player 2 win")
            break
        elif p2 == 3:
            print("Player 1 win")
            break
        else:
            print("Try again")
    
    if p1 == 2:
        if p2 == 1:
            print("Player 1 win")
            break
        elif p2 == 3:
            print("Player 2 win")
            break
        else:
            print("Try again")
    
    if p1 == 3:
        if p2 == 2:
            print("Player 1 win")
            break
        elif p2 == 1:
            print("Player 2 win")
            break
        else:
            print("Try again")