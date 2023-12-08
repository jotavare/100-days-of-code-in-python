#import 'art' and 'game_data' files
#import replit 'clear()' and random modules
from art import logo, vs
from game_data import data
from replit import clear
import random

#choose a random dictionary from the list 'data' in 'game_data.py'
#randomize two times and assign to two different variables
a_random_data = random.choice(data)
b_random_data = random.choice(data)

#define a variable called score with a value of 0
#define a variable called condition with a bollean value of True
score = 0
condition = True


#define a function to print the current random data
#this will print 3 values from the 'a_random_data' and 'b_random_data'
def print_data():
    """This will print the current a_random_data and b_random_data data."""
    print(
        f"A: {a_random_data['name']}, a {a_random_data['description']}, from {a_random_data['country']}."
    )
    print(vs)
    print(
        f"\nB: {b_random_data['name']}, a {b_random_data['description']}, from {b_random_data['country']}."
    )


#create a while loop that will only stop if the user
#writes the wrong answer
while condition:

    #print the logo and call the function that prints the messages
    print(logo)
    print_data()

    #the score will only print if the value is > 0
    if score > 0:
        print(f"\nCurrent score: {score}")

    #ask the user for a input of "who has more followers ?"
    #save to a variable called 'answer' and transform to uppercase
    #to avoid lower case letters
    answer = input("\nWho has more followers? Type 'A' or 'B': ").upper()

    #if 'answer == A', compare A 'followers' with B 'followers' and vice-versa
    #if the user answer is >, then change score to '+=1' and print a message
    #assign the data 'b_random_data' to 'a_random_data'
    #and assign a new data to 'b_random_data' and clear the console
    if answer == "A":
        if a_random_data['follower_count'] > b_random_data['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}.")
            a_random_data = b_random_data
            b_random_data = random.choice(data)
            clear()
        #if the answer is <, then 'clear' console and print 'logo'
        #this will also change the 'condition = False' to stop the loop
        #print a message with the current 'score' and end
        elif a_random_data['follower_count'] < b_random_data['follower_count']:
            condition = False
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")

    #same thing as above but the 'answer == B'
    elif answer == "B":
        if b_random_data['follower_count'] > a_random_data['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}.")
            a_random_data = b_random_data
            b_random_data = random.choice(data)
            clear()

        elif b_random_data['follower_count'] < a_random_data['follower_count']:
            condition = False
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")

    #else, if the user writes anything not equal to "A" or "B"
    #print a custom message, change 'condition' to 'False' and end
    else:
        condition = False
        clear()
        print("Invalid choice!")
