# create a blind action
from replit import clear
from art import logo

# print ascii logo and the game goal
print(logo)
print("This is a blind auction, you can input your name and bid.")
print(
    "After that, pass the computer to other person and find who's the highest bidder!"
)

# create a empty dictionary and set a value for bidding_finished
bids = {}
bidding_finished = False


# define a function
def find_highest_bidder(bidding_record):

    # set the highest bid as 0 and create a winner atribute
    highest_bid = 0
    winner = ""

    # check if the current user bid is the highest
    # print the result if the user type "no" to repeat
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# create a lop that will store user inputs
while not bidding_finished:

    # ask for name, price
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    bids[name] = price

    # ask the user to repeat
    should_continue = input(
        "Are there any other bidders? Type 'yes or 'no'.\n")

    # if "no", change bidding_finished to True and print result
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)

    # if "yes", clear console and repeat loop
    elif should_continue == "yes":
        clear()
