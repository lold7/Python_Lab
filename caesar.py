letter = "abcdefghijklmnopqrstuvwxyz"

def my_input():
    print("Fill word")
    word = input(": ")
    word = word.lower()
    word = list(word)
    return word

def my_encrypt(word_list):
    for i in range(len(word_list)):
            for j in range(len(letter)):
                if word[i] == letter[j]:
                    new_w = letter[j+3]

            word[i] = new_w
    
    return word


def my_decrypt(word_list):
    for i in range(len(word_list)):
            for j in range(len(letter)):
                if word[i] == letter[j]:
                    new_w = letter[j-3]

            word[i] = new_w
    
    return word



while True:
    print("Enter e to encrypt or Enter d to decrypt or Enter q to quit program")
    mode = input(": ")
    mode = mode.lower()
    
    try:
        if mode not in ("e","d","q"):
            raise Exception ("Plase choose mode")
    except Exception as err:
            print(err)

    if mode == "q":
        print("Quit Program")
        break

    elif mode == "e":
        word = my_input()
        word = my_encrypt(word)
        word = "".join(word)
        print(f"word are encrypted: {word}")
             
    elif mode == "d": 
        word = my_input()
        word = my_decrypt(word)
        word = "".join(word)
        print(f"word are decrypted: {word}")

    

    

    