# Day 9
from os import system
from art import gavel_logo

print(f"{gavel_logo}\nWelcome to the secret aution program.")

bidders = {}
bid_complete = True

def highest_bidder(bidders):
    # placeholders
    highest_bid = 0
    bidder_name = ""
    # find highest bidder
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            highest_bid = bidders[bidder]
            bidder_name = bidder
    print(f"The highest bidder is: {bidder_name} with a bid of {highest_bid}.")

while bid_complete:
    # inputs
    name = input("What is your name?: ")
    bid = input("What is your bid?: ")
    # removing $, convert to int
    bid = int(bid.replace("$", ""))
    # add to dictionary
    bidders[name] = bid
    # add more 
    more_bidders = input("Are there more bidders?\n").lower()
    if more_bidders == "yes":
        system('clear')
    else:
        bid_complete = False
        highest_bidder(bidders)