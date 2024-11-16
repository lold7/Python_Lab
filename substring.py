def substr(string,start,stop = None):
    if stop == None:
        stop = len(string)
    return string[start:stop+1]

def substr_len(string,start,len):
    string = str(string)
    len = len + start
    return string[start:len]

print(substr("Earth",0,3))
print(substr_len("I like python and C#",5,3))