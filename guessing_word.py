import random

animals = [
    "Lion",
    "Tiger",
    "Elephant",
    "Giraffe",
    "Zebra",
    "Kangaroo",
    "Panda",
    "Wolf",
    "Bear",
    "Dolphin",
    "Whale",
    "Penguin",
    "Eagle",
    "Owl",
    "Cheetah",
    "Hippopotamus",
    "Rhinoceros",
    "Chimpanzee",
    "Crocodile",
    "Flamingo"
]

random_word = random.choice(animals)
life = 4

index_list = []

print(f"Life: {life}")
while True:
    if life == 4:
        puzzle_line = "_" * len(random_word)
        puzzle_line = " ".join(puzzle_line)
        puzzle_line = puzzle_line.strip()
        print(puzzle_line)
    elif life <4:
        index_random = random.randint(0,len(random_word)-1)
        while index_random in index_list:
            index_random = random.randint(0,len(random_word)-1)
        index_list.append(index_random)
        puzzle_line = puzzle_line.replace(" " , "" )
        puzzle_line = list(puzzle_line)
        random_word = list(random_word)
        char = random_word[index_random]
        puzzle_line[index_random] = char
        puzzle_line = " ".join(puzzle_line)
        puzzle_line = puzzle_line.strip()
        random_word = "".join(random_word)
        print(puzzle_line)


    word_input = input("Enter word: ")

    if word_input == random_word:
        print("You win!!!")
        print(f"Answer: {random_word}")
        break
    elif word_input != random_word:
        print("Try again")
        life -= 1
        if life == 0:
            print(f"Life: {life}")
            print("Your lost")
            print(f"Answer: {random_word}")
            break
        print(f"Life: {life}")
