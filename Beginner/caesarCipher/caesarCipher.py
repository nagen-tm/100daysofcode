# Day 8
import string
from art import logo

# logo/variables
print(logo)
alphabet = string.ascii_lowercase
rerun = True

def caesar_cipher(direction, text, shift):
    resulting_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if not char.isalpha():
            resulting_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift
            new_letter = alphabet[new_position]
            resulting_text += new_letter.lower()
    print(f"The {direction}d text is {resulting_text}")

# allows a rerun of the program 
while rerun:
    # inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt.:\n")
    text = input("Type your mesage:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # allows for shifts greater than list
    shift = shift % 26
    caesar_cipher(direction, text, shift)
    # input for rerun, 
    rerun_input = input("Type 'yes' if you want to go again. Otherwise hit any key to exit.\n").lower()
    if rerun_input != 'yes':
        rerun = False
        print("Goodbye.")

