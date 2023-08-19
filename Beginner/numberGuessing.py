from random import randint

#pseudo code:
# guessing a number from 1 -100, randomize 
# difficulty modes, easy or hard, changes number of guesses 5
# tells if guess is too high or too low
# either answer is guessed or attempts are reached, return win or lose

# difficulty input and setting number of guesses
def difficulty():
    '''Returns the number of guesses per difficulty.'''
    mode = input("Choose a difficulty, 'easy' or 'hard': ").lower()
    if mode == 'easy':
        return 10
    elif mode == 'hard':
        return 5
    else:
        return 'error'
 
def number_check(guess, random_number):
    '''Returns int 1 for too high or low, 2 for correct answer.'''
    if guess > random_number:
        print("Your guess is too high, guess again.")
        return 1
    elif guess < random_number:
        print("Your guess is too low, guess again.")
        return 1
    else:
        return 2

def game():
    '''Play through number guessing game.'''
    # create the random number
    random_number = randint(1, 101)
    print("Welome to the Number Guessing Game!\nI'm thining of a number between 1 and 100.")
    turns = difficulty()
    if turns == "error":
        print("Error, please choose correct difficulty.")
        turns = difficulty()
    # loop through turns until guessed or no more turns
    while turns > 0:
        guess = int(input("What is your guess?: "))
        if number_check(guess, random_number) == 1:
            turns -= 1
            print(f"You have {turns} attempts remaining to guess the number.")
        else: 
            turns = 0
            print("You've guessed the correct number, congrats!")


game()