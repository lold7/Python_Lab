sentance = """
Happy Birthday to you,
Happy Birthday to you,
Happy Birthday day,
Happy Birthday to you!
"""
count = 0
words = sentance.split()

words = [i.lower() for i in words]

for i in words:
    if i == "happy":
        count += 1

print(f"Happy: {count}")