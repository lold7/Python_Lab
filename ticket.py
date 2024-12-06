tic_dic = {1:30 , 2:70 , 3:40 , 4: 80, 5:50 ,6:0}


while True:
    try:
        st = int(input("Station Start: "))
        en = int(input("Station End: "))
        if st not in range(1, 7) or en not in range(1, 7):
            raise Exception ("Please fill only Station 1 - Station 6")
        
        if st > en:
            keep = en
            en = st
            st = keep  

        expense = 0
        for i in range(st,en+1):
            expense += tic_dic[i]
        print(f"Total Expenses: {expense}")
        break

    except Exception as err:
        print(err)
        print("Try again")

  
