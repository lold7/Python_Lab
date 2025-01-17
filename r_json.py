import json
with open("my_j.json" , mode="r+") as r:
    read = json.load(r)
    print(read)