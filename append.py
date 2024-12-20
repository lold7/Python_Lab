def func(**k):
    result = []
    if k.get("Lubu"):
        result.append(k["Lubu"]) # k["Lubu"] == "warrior"
    elif k.get("Teeme"):
        result.append(k["Teeme"])
    print(result)


func(Lubu = "warrior")
func(Teeme = "Midlane")

