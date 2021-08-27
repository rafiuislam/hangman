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

    lives = 7

    while len(letters_word) > 0 and lives > 0:
        print(f'{lives}, lives remaining and letters already used: ', ' '.join(letters_used))

        list_of_word = [letter if letter in letters_used else '-' for letter in word]
        print(f'Current Word: ', ' '.join(list_of_word))

        user_letter = input("Guess a Letter: ").upper()
        if user_letter in alphabet - letters_used:
            letters_used.add(user_letter)
            if user_letter in letters_word:
                letters_word.remove(user_letter)
            else:
                lives -= 1
                print('Letter not found in word!')
        
        elif user_letter in letters_used:
            print("Please try again, (already used that letter).")

        else: 
            print("Please try again, (Invalid character).")

    if lives == 0:
        print(f"Please try again, the word was: {word}")
    else:
        print(f"Congrats!! you guessed correctly, the word was: {word}")

hangman()