for i in range(2016,2201):
    if (i % 400 == 0) or (i % 100 != 0 and i % 4 == 0):
        print(f"{i} is Leap Year")

