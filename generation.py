year_born = int(input("Enter your year born: "))

if year_born <= 2433:
    gen = "Lost Generation"
elif year_born >=2444 and year_born <=2467:
    gen = "Greatest Generation"
elif year_born >=2468 and year_born <= 2488:
    gen = "Silent Generation"
elif year_born >=2489 and year_born <= 2507:
    gen = "Baby Boomer Generation"
elif year_born >= 2508 and year_born <= 2519:
    gen = "Generation X"
elif year_born >= 2520 and year_born <= 2538:
    gen = "Generation Y"
elif year_born >= 2539 and year_born <= 2555:
    gen = "Generation Z"
else:
    gen = "Alpha Generation"

print(gen)