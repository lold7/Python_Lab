import random

print("--------Sales in 7 days--------")

for i in range(1,8):
    print(f"Day {i} |",end=" ")
    sale_random = random.randint(1,20)
    print(("*" * sale_random)+f"({sale_random})")