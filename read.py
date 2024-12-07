try:
    x = open("simple.txt" , mode = "r" , encoding="utf-8")
    print(x.read())

    x.seek(0)
    print(x.read(10))

except IOError as err:
    print(err)

else:
    x.close()