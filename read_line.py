try:
    txt = open("simple.txt" , "r+" , encoding= "utf-8")
    read1 = txt.readline()
    print(read1)
    
    read2 = txt.readline()
    print(read2)

except IOError as err:
    print(err)

else:
    txt.close()