import random

char1 = "1234567890"
char2 = "abcdefghijklmnopqrstuvwxyz"
char3 = char2.upper()

all_char = char1 + char2 + char3

pin = ""
for i in range(0,6):
    pin += random.choice(all_char)

print(pin)