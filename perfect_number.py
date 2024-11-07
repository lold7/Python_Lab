for i in range(1,9001):
    mod = 0
    for j in range(1,i):
        if i % j == 0:
            mod += j
    if mod == i:
        perfect = mod
        print(perfect)
