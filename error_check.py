try:
    print(data)
    result = "a" + 1

except TypeError :
    print("Type is not match")
except NameError:
    print("Don't declare variable yet") 
finally:
    print("fuck")