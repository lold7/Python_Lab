code_format = input("Enter code(*9999*XXXXXXXXXX#): ")
if len(code_format) >17 or len(code_format) < 17:
    raise Exception ("Code incorrect")

for i in range(0,len(code_format)):
    if i == 0 or i == 5:
        if i != "*":
            print("Code incorrect")
            break
    elif i in range(1,5):
        if i != "9":
            print("Code incorrect")
            break
    elif i in range(6,16):
        if i not in range(0,10):
            print("Code incorrect")
            break
    elif i == 16:
        if i != "#":
            print("Code incorrect")
            break
    else:
        print(f"Your code: {code_format}")
        break
