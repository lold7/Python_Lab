count = 0

while True:
    x = input("Enter: ")
    x = x.lower()

    if x == "q":
        print("Quit Program")
        break

    elif x =="r":
        count = 0
        print("Reset")
        print(count)

    else:
        count += 1
        print(count)
        