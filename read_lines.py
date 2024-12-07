try:
    with open("simple.txt" , mode="r+" ,encoding="utf-8") as x:
        read = x.readlines()
    
    for i,j in enumerate(read):
        read[i] = j.strip("\n")
    
    print(read)
except IOError as err:
    print(err)