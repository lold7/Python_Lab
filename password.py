password = "1234"
count = 1
count_dic = {1:"1st time",2:"2nd time",3:"3re time"}


while True:
    pass_input = input("Enter Password: ")
    if count == 4:
        print("Enter password 3 times.Password is canceled")
        break 
    elif pass_input != password:
        print(f"{count_dic[count]} : incorrect")
        count += 1
    else:
        print("Correct")
        break