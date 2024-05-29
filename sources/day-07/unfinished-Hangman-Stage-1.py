#step 1 of hangman
#import random module
import random

#create a list
word_list = ["apple", "computer", "light", "jacket"]

#randomly choose a word from the word_list and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)

#ask the user to guess a letter and assign their answer to a variable called guess and make guess lowercase
letter = input("Guess a letter: ").lower()

#check if the letter the user guessed (guess) is one of the letters in the chosen_word
value = 0

for guess in range(0, len(chosen_word)):
    if letter == chosen_word[value]:
        print("Right!")
        value += 1
    else:
        print("Wrong!")
        value += 1