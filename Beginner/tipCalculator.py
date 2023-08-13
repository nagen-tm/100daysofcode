# Day 2

# Create tip calculation for data types
print("Welcome to the tip calculator.")
total = input("What was the total bill?")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15?")
split = input("How many people to split the bill?")

percentage = float(tip_percentage) / 100
total_with_tip = (float(total) * percentage) + float(total)
split_per_person = round(total_with_tip / int(split), 2)

print(f"Each person should pay: {split_per_person}")