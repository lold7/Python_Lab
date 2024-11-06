balance = 1000000
print(f"Balance is {balance:,}")

withdraw = int(input("Amount to withdraw: "))

if balance < withdraw:
    print("Money not enough")
elif withdraw > 20000:
    print("Withdraw must equal or less than 20000")
elif withdraw % 100 != 0:
    print("Withdraw must be whole hundreds number")
else:
    balance = balance-withdraw
    print(f"Withdraw: {withdraw:,}\nBalance: {balance:,}")
