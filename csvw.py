import csv

try:
    with open("simple.csv" , mode= "w+" ,encoding="utf-8") as file:
        #declare object
        write = csv.writer(file)

        write.writerow(
            ["Earth" , "6/4" , "01"]
        )

        write.writerows([["Wood" , "6/4","02"],
                        ["Wim" ,"6/4","03"]])
        
except IOError as err:
    print(err)