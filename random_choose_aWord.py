import random
word_list = ["arward","baboon","camel"]
chosen_word = random.choice(word_list)

guess = input(" Guess a word : ").lower()

for letter in chosen_word:
    if letter == guess :
        print(" Right ! ")
    else :
        print("wrong !")    
    
