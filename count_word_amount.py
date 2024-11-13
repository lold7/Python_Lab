word = input("Enter word: ")

word_dic = {}

for i in word:
    if i == " ":
        continue

    if i in word_dic:
        word_dic[i] += 1
    else:
        word_dic[i] = 1

for j in word_dic:
    print(f"{j} : {word_dic[j]}")