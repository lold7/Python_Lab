word = "abcdefghijklmnopqrstuvwxyz"
result=""
num = int(input("Enter number: "))

for i in range(num):
    result = result + word[i]

print(result)
