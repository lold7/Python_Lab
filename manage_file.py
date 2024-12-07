import os

try:
    with open("old_file.txt" , mode="a+") as file:
        print(
            file.readable(),
            file.writable(),
            file.seekable(),
            sep="\n"
        )
except IOError as err:
    print(err)


try:
    x = os.path.isfile("simple.txt")
    y = os.path.isdir("csvr.py")
    z = os.path.getsize("tex.py")

    if not(os.path.exists("assert.py")):
        raise OSError ("Don't have this file")
    else:
        print(os.path.exists("assert.py"))
    

    os.rename("name.png","QRcode.png")
    
except IOError as err:
    print(err)
