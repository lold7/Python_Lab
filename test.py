my_list = ["a", "b", "c", "d"]
iterator = iter(my_list)  # Convert the list into an iterator

for i in range(2):
    next(iterator)

print(*iterator)

# If you call `next(iterator)` again, it will raise `StopIteration`.
