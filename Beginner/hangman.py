# Day 7
import random
from os import system
from art import hangman_logo, stages

# pick random word, set variables
#TO DO: create a word list to import
word_list = ["ardvark", "baboon", "camel"]
word_selection = random.choice(word_list)
display = [] 
lives = 6
end_of_game = False

# check letter in word
for letter in word_selection:
    display.append("_")

print(hangman_logo)

# get input 
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # clear the screen 
    system('clear')
    # if letter was already guessed, tell user
    if guess in display:
        print(stages[lives])
        print(f"You already guessed {guess}.")
    else:
        # check letter for each position
        for position in range(len(word_selection)):
            letter = word_selection[position]
            if letter == guess:
                display[position] = letter
        # lose life if guess is wrong
        if guess not in word_selection:
            print(f"{guess} is not in the word. You lose a life.")
            lives -= 1
            # end game at 0 lives
            if lives == 0: 
                end_of_game = True
                print("You lose.")
        # end game if guessed word
        if "_" not in display:
            end_of_game = True
            print("You win.")
        print(stages[lives])
        print(f"{' '.join(display)}")