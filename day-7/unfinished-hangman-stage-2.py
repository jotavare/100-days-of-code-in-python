#step 1 of Hangman
#import random module, create a list and choose one at random
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#testing code
print(f'Pssst, the solution is {chosen_word}.')

#create an empty List called display.
#for each letter in the chosen_word, add a "_" to 'display'.
#so if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
guess = input("Guess a letter: ").lower()
display = []

for space in range(0, len(chosen_word)):
    display += "_"

print(display)

#loop through each position in the chosen_word;
#if the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
value = 0

for letter in chosen_word:
    if letter == guess:
        display[value] = guess
        value +=1
        print("Right")
    else:
        print("Wrong")
        value +=1

#print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
print(display)