# Day 11
# Blackjack Rules for this Project
# The deck is unlimited size. There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn

# ISSUES: the Ace being 1 or 11 doesn't seem to work for computer
# how can i use AKQJ instead of 10s 

import random
from os import system
from art import blackjack_logo

# build the logic on the cards
def deal_card():
    """Returns random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7 ,8 ,9 ,10, 10, 10, 10] 
    card = random.choice(cards)
    return card

def add_cards(cards):
    """Returns total score of user's cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and len(cards) == 2:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def results(player_score, computer_score):
    if player_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "You lose, computer has Blackjack."
    elif player_score == 0:
        return "You win with Blackjack!"
    elif player_score > 21:
        return "Bust! You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    else:
        return "You lose."


def blackjack():
    print(blackjack_logo)
    # placeholders for hands
    player_cards = []
    computer_cards = []
    # randomize what you and the computer gets
    for card in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    # while loop to continue getting cards
    continue_hit = True
    while continue_hit:
        # display the cards
        print(f"Your cards: {player_cards} Current score: {add_cards(player_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if hit == "y":
            player_cards.append(deal_card())
            if add_cards(player_cards) > 21:
                continue_hit = False
        else:
            continue_hit = False

    computer_score = add_cards(computer_cards)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = add_cards(computer_cards)
        
    print(f"Your final hand: {player_cards}")
    print(f"Computer's final hand: {computer_cards}")
    player_score = add_cards(player_cards)
    print(results(player_score, computer_score))

while input("Do you want to play Blackjack? Type 'y' or 'n': ").lower() == 'y':
    system('clear')
    blackjack()
