num_list = ["zero","one" , "two" , "three" , "four" , "five" , "six" ,"seven","eight" , "nine" ]

while True:
    try:
        num = int(input("Enter number(0-9): "))
    except:
        print("Please Enter number(0-9)")
        continue

    if num > 9 or num < 0:
        print("Please Enter number(0-9)")

    else:
        read = num_list[num]
        print(f"Read: {read}")
        break