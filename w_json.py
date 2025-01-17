import json


object = {"cpu" : "AMD" , "gpu": "intel arc" ,
          "Ram" : {"4" : "very slow" , "8": "slow" , "16":"OK" , "32":"good"}}

with open("my_j.json" ,mode="w+") as w:
    json.dump(object,w,indent = 4)