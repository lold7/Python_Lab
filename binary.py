import pickle

try:
    with open("simple.bin" ,mode = "wb+") as x:

        #write text to the file
        pickle.dump("dog",x) 
        pickle.dump("cat",x)
except IOError as err:
    print(err)


try:
    with open("simple.bin",mode= "rb+") as x:

        #read binary file
        print(
            pickle.load(x),
            pickle.load(x),
            sep="\n"
        )
except IOError as err:
    print(err)
        

        