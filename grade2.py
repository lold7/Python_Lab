import random

score = random.randint(1,100)

print(f"Score: {score}",end=" ")
if score >= 80:
    print('Grade A')
elif score >= 70:
    print('Grade B')
elif score >= 60:
    print('Grade C')
elif score >= 50:
    print('Grade D')
else:
    print('Grade F')
