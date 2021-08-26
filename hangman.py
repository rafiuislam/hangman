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

    while len(letters_word) > 0:
        print('Letters already used: ', ' '.join(letters_used))

        list_of_word = [letter if letter in letters_used else '-' for letter in word]
        print(f'Current Word: ', ' '.join(list_of_word))

        user_letter = input("Guess a Letter: ").upper()
        if user_letter in alphabet - letters_used:
            letters_used.add(user_letter)
            if user_letter in letters_word:
                letters_word.remove(user_letter)
        
        elif user_letter in letters_used:
            print("Please try again, (already used that letter).")

        else: 
            print("Please try again, (Invalid character).")

    print(f"The word was {word}")

hangman()