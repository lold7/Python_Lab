import csv
result = []
with open("icsv.csv" , mode= "r+" , encoding="utf-8" ) as r:
    read = csv.reader(r)
    for _ in range(7):
        next(read)
    
    for i in read:
        i = " ".join(i)
        print(i)
          

  
    