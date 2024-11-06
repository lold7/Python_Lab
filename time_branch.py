second_input = int(input("Enter second: "))

hour = second_input // 3600
hour_remain = second_input % 3600

minutes = hour_remain // 60
second = hour_remain % 60

print(f"{hour} : {minutes} : {second}")