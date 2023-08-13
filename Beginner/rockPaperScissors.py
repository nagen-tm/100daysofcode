# Day 4
import random

scissors = '''
    _____
---'   ___)___
        ______)
       ________)
      (___)
---.__(__)
'''

rock = '''
    _____
---'   ___)
      (____)
      (____)
      (___)
---.__(__)
'''

paper = '''
    _____
---'   ___)___
        ______)
       ________)
       _______)
---._________)
'''
imgages = [rock, paper, scissors]

# user input
choice = int(input("What do you choose: 0 for rock, 1 for scissors, and 2 for paper.\n"))
if choice > 2:
    print("Please pick a number 0, 1, or 2.")
    exit()
print("Your choice:")
print(imgages[choice])

# random choice
computer_choice = random.randint(0, 2)
print("Computer choice:")
print(imgages[computer_choice])

# who wins
if choice == computer_choice: 
    print("It's a draw!")
elif (choice == 0 and computer_choice == 1) or (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 0): 
    print("You win.")
else:
    print("You lose.")
