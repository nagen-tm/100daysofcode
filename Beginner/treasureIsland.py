# Day 3
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

choice_one = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()

if choice_one == "left":
    choice_two = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if choice_two == "wait":
        choice_three = input("A boat picks you up and you get dropped off at the island.\nThere is a house with 3 doors. One red, one yellow, one blue. Which color do you choose?\n").lower()
        if choice_three == "yellow":
            print("You have found the treasure. Pay off your debt!")  
        elif choice_three == "blue":
            print("A ghost possesses you. Game Over.")  
        else:
            print("A werewolf attacks you. Game Over.")
    else:  
        print("You die of hypothermia. Game Over.")  
else:
    print("You fell off a cliff. Game Over.")


