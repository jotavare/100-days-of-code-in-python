#step 3 of Hangman
#import module, create list, randomize and lenght the chosen word
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#testing code
print(f'Pssst, the solution is {chosen_word}.')

#create blank list and list with "_"
display = []
for _ in range(word_length):
    display += "_"

#use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while "_" in display:
    guess = input("Guess a letter: ").lower()

#check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
else:
    print("You Won!")

print(display)