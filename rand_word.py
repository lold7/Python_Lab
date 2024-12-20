import random

letter = "abcdfg"
char_T = random.choice(letter)
life = 4

while True:
    if life == 0:
        print(f"life = {life}")
        print("Your Lost")
        break


    guess = input("Enter: ")
    
    if guess == char_T:
        print(f"You win answer: {letter}")
        break
    elif guess != char_T:
        life -= 1
        print("not currect")
        print(f"Your life:{life}")


