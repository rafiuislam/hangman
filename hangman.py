import random
import string
from words import words 

def get_gapless_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word =random.choice(words)
    
    return word.upper()

def hangman():
    word = get_gapless_word(words)
    letters_word = set(word) 
    letters_used = set() # user guessed
    alphabet = set(string.ascii_uppercase)

    user_letter = input("Guess a Letter: ").upper()

    if user_letter in alphabet - letters_used:
        letters_used.add(user_letter)
        if user_letter in letters_word:
            letters_word.remove(user_letter)
    
    elif letters_word in letters_used:
        print("Please try again, (already used that letter).")

    else: 
        print("Please try again, (Invalid character).")


user = input('Please input something: ')
print(user)