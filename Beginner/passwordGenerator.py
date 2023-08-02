import random
import string

# create lists of letters, numbers, and symbols
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# input
print("Welcome to the PyPassword Generator.")
num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))

# logic
password = []
for i in range(num_letters + 1):
    password += random.choice(letters)
for i in range(num_numbers + 1):
    password += random.choice(numbers)
for i in range(num_symbols + 1):
    password += random.choice(symbols)

# randomization of the characters
random.shuffle(password)
password = ''.join(password)

# result
print(f"Here is your password: {password}")