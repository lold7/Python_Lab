date_str = input("Enter date (Day / Month / Year): ")
split = date_str.split("/")

try:
    assert split[0] in range(1,32) , "Day must be 1 - 31"
    assert split[1] in range(1,13) , "Month must be 1 - 12"
    assert split[2] in range(1,10001) , "Year must be 1 - 10000"

except Exception as err:
    print(err)

