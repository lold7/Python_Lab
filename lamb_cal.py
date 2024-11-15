def calculator(func,*num):
    return func(*num)


add = lambda x,y: x+y
subtract = lambda x,y: x-y
multi = lambda x,y:x*y
divi = lambda x,y:x/y


result_add = calculator(add, 10, 20)
print("Addition:", result_add)

result_subtract = calculator(subtract, 20, 10)
print("Subtraction:", result_subtract)

result_multi = calculator(multi, 10, 5)
print("Multiplication:", result_multi)

result_divi = calculator(divi, 20, 4)
print("Division:", result_divi)