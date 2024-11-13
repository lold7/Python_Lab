A_Z = range(ord("A"),ord("Z")+1)
a_z = range(ord("a"),ord("z")+1)
a0_9 = range(ord("0"),ord("9")+1)

check_1 = False
check_2 = False
check_3 = False

password = input("Enter password: ")

ord_list = []
for i in password:
    j = ord(i)
    ord_list.append(j)

for i in ord_list:
    if i in A_Z:
        check_1 = True
    if i in a_z:
        check_2 = True
    if i in a0_9:
        check_3 = True

if check_1 and check_2 and check_3:
    print(f"Your password: {password}")
else:
    print("Pass must consist A-Z, a-z, 0-9")
