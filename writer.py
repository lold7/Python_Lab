try:
    with open("simple.txt" , mode="a+" ,encoding="utf-8") as wri:
        wri.write("1 ")
        wri.write("2 ")
        wri.write("3 ")
        num_list = ["4 ","5 ","6 ","7 ","8 ","9 ","10 "]
        wri.writelines(num_list)


except IOError as err:
    print(err)