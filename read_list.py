with open("simple.txt" , mode= "r+" , encoding="utf-8") as r:
    read = [i.strip() for i in r.readline()]
    print(read)