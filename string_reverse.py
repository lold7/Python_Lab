def reverse(str):
    x = list(str)
    x.reverse()
    x = "".join(x)
    return x

string = input("Enter string: ")
print(reverse(string))

