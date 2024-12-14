def prime(i):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count +=1

    if count == 2:
        return True
    else:
        return False


for i in range(2,101):
    if prime(i):
        print(i)
    else:
        continue