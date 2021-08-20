#import the ascii logo and random modules
from art import logo
import random

#print logo and welcome message
print(logo)
print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")

#ask the user difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

#create a variable with a random number (1-100)
random_number = random.randint(1, 100)

#number of attemps the user as
attempts = 0


#define how many attempts the user based on answer
def lifes():
    #transform "attempts" in a global variable
    global attempts

    if difficulty == 'easy':
        attempts = 10
        return "\nYou have 10 attempts to guess the number."

    elif difficulty == 'hard':
        attempts = 5
        return "\nYou have 5 attempts to guess the number."

    else:
        return "Invalid answer."


#user guess, compare the two numbers and give a output
def compare():
    #define attempts as a global so i can access it
    global attempts

    #ask the user to make a guess, compare and loop
    user_number = int(input("Make a guess: \n"))
    if attempts > 1:
        if user_number != random_number:
            if user_number > random_number:
                print("\nToo high.")
                print("Guess again.")
                attempts -= 1
                print(
                    f"You have {attempts} attempts remaining to guess the number."
                )
                compare()

            elif user_number < random_number:
                print("\nToo low.")
                print("Guess again.")
                attempts -= 1
                print(
                    f"You have {attempts} attempts remaining to guess the number."
                )
                compare()

        else:
            print(
                f"\nYou got it! The answer was {random_number}.\nCongratulations!"
            )

    elif user_number > random_number:
        print("\nToo high.")
        print("You've run out of guesses, you lose.")

    elif user_number < random_number:
        print("\nToo low.")
        print("You've run out of guesses, you lose.")


#call both functions
#by printing the function i am also returning the value
print(lifes())
compare()
