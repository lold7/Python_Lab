people_amount = int(input("Amount of people: "))

sum_rating = 0

for i in range(1,people_amount+1):
    while True:
        rating = int(input(f"People {i} enter rating 1 - 5: "))
        if rating > 5:
            print("Rating must be 1 - 5 only!!!\nTry again")
        else:
            break
    sum_rating += rating

average = sum_rating/(people_amount*5)
show_aver = (format(average,".2f"))
print(f"Average: {show_aver}")


if 1.0 >= average >= 0.8 :
    print("rating: *****")
elif 0.79 >= average >= 0.6 :
    print("rating: ****")
elif 0.59 >= average >= 0.4 :
    print("rating: ***")
elif 0.39 >= average >= 0.2:
    print("rating: **")
else:
    print("rating: *")