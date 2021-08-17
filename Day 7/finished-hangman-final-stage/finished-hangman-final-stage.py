#final step of hangman
import random
import hangman_art
import hangman_words

#update the word list to use the 'word_list' from hangman_words.py
#delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

#testing code
print(f'Pssst, the solution is {chosen_word}.')

#create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #if the user has entered a letter they've already guessed, print the letter and let them know.       
    if guess in display:
        print(f"You've already guessed {guess}.")

    #check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #check if user is wrong.
    if guess not in chosen_word:
        #if the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])