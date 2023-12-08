#import 'random' module, the logo from 'art.py' and 'clear()' function
import random
from replit import clear
from art import logo

#create a list with all the values of blackjack
#10 repeats 4 times to represent queen, king and jack
#chooses a random card and return it as 'card'
def deal_card():
    """returns a random card from the list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#calculates all the values in a list and return it as 'cards'
def calculate_score(cards):
    """calculate the score from the list of cards"""

    #if score is 21 return as '0' to represent a blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    #if there's 2 aces (11,11), remove one value and assign it as 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    #returns the sum of the function parameters
    return sum(cards)

#compares the scores from user and computer
#returns a custom message based on the if statements
def compare(user_score, computer_score):
    """"""
    if user_score == computer_score:
        return " Draw!\n"
    elif computer_score == 0:
        return " You Lose! The computer has a Blackjack.\n"
    elif user_score == 0:
        return " You Won! You got a Blackjack.\n"
    elif user_score > 21:
        return " You went over 21. You Lose!\n"
    elif computer_score > 21:
        return " Computer went over 21. You Win!\n"
    elif user_score > computer_score:
        return " You Won!\n"
    else:
        return " You Lose!\n"

#this function only exists to loop the game
def play_game():

    #prints the ascii blackjack logo
    print(logo)

    #creates a empty list of user and pc random chosen cards
    #assigns a boolean value to 'game_over'
    user_cards = []
    computer_cards = []
    game_over = False

    #loops 2 times, calls the function 'deal_card'
    #assigns the values to the user and computer lists
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #just a while loop to repeat this section
    while not game_over:

        #call the function to calculate the user and computer score and assign a variable
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        #print the user cards, computer first card and total score
        print(f"\n Your cards: {user_cards} = {user_score}")
        print(f" Computer first card: {user_cards[0]}\n")

        #checks if user or computer got a blackjack or 21, if so the game ends
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        #ask for the user if it wants another card
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")

            #this will call the function 'deal_card' and save the new number into 'user_cards' list
            if user_should_deal == "y":
                user_cards.append(deal_card())

            #they didn't type "y", so the game ends by changing the variable to 'game_over' True
            else:
                game_over = True

    #while the computer is not equal to a blackjack (0) or less than 17
    #it should draw more cards with the 'deal_card' function and save it to 'computer_score'
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    #print both user and computer final hands and the result
    print(f"\n Your final hand: {user_cards} = {user_score}")
    print(f" Computer final hand: {computer_cards} = {computer_score}\n")
    print(compare(user_score, computer_score))

#while the input = 'y' this will clear the console
#call the function 'play_game()' so the game loops
while input("Do you want to play a game of Black Jack. Type 'y' or 'n': ") == "y":
    clear()
    play_game()