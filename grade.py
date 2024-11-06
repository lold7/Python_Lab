score = int(input("Enter your score(0 - 100): "))

if score >= 80:print(f"{score} >> A")
elif score >= 70:print(f"{score} >> B")
elif score >= 60:print(f"{score} >> C")
elif score >=50:print(f"{score} >> D")
else:print(f"{score} >> F")