rude_word = ["xxx","yyy","zzz"]

word = input("Enter word: ")
word.lower()

for i in rude_word:
    sen = "*" * len(i)
    word = word.replace(i,sen)

print(word)