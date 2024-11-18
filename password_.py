password = input("Enter password: ")

if len(password) < 7 and len(password) >20:
    print("Password must have 7-20")
    password = ""

A_Z  = range(ord("A"),ord("Z")+1)
a_z  = range(ord("a"),ord("z")+1)
num  = range(ord("0"),ord("9")+1)
num_count = 0

text_err = ""

check1 = False
check2 = False
check3 = False
text_bool = True

ord_list = [ord(i) for i in password]

for i in range(0,len(ord_list)):
    if ord_list[i] in A_Z:
        check1 = True
    
    elif ord_list[i] in a_z:
        check2 = True

    elif ord_list[i] in num:
        num_count += 1
        check3 = True
    else:
        char = chr(ord_list[i])
        text_err += char

if text_err != "":
    maek_set = set(text_err)
    print(f"Error: {", ".join(maek_set)}")
    text_bool = False

    

if num_count >= 2:
    num_count = True


if check1 and check2 and check3 and num_count and text_err:
    print(f"Your password is: {password}")

else:
    print(f"Password must consist A-Z, a-z and 0-9 only")