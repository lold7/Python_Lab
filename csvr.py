import csv

try:
    with open("simple.csv" , mode= "r+" ,encoding="utf-8") as file:
        #declare object
        read = csv.reader(file)

        print(*read)

except IOError as err:
    print(err)