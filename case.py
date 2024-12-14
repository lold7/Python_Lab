print("1 >>> Python")
print("2 >>> Java")
print("3 >>> C")

num = input("Choose number: ")


match num:
    case "1": print("Python")
    case "2": print("Java")
    case "3": print("C")