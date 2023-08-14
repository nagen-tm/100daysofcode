# Day 11
# Blackjack Rules for this Project
# The deck is unlimited size. There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn

import random

# build the logic on the cards
# TO DO: figure out the 11 or 1 ace
cards = [11, 2, 3, 4, 5, 6, 7 ,8 ,9 ,10, 10, 10, 10]
def add_cards(cards):
    total = 0
    for card in cards:
        total += card
    return total

# placeholders for hands
player_cards = []
computer_cards = []

def blackjack():
    # randomize what you and the computer gets
    for card in range(0, 2):
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    # display the cards, get input
    print(f"Your cards: {player_cards}")
    print(f"Computer's first card: {computer_cards[0]}")
    hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    
    if hit == "y":
        player_cards.append(random.choice(cards))
    else:
        print(f"Your final hand: {player_cards}")
        print(f"Computer's final hand: {computer_cards}")
        player_score = add_cards(player_cards)
        computer_score = add_cards(computer_cards)
        if player_score > computer_score and player_score < 21:
            print("You win!")
        elif player_score == computer_score: 
            print("It's a draw.")
        else:
            print("You lose!")


blackjack()
