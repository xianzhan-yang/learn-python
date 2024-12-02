# Ask for the user's name
name = input("What is your name? ")

# Ask for the user's age
age = int(input("How old are you? "))

# Calculate the year they'll turn 100
current_year = 2024
turn_year = current_year + (100 - age)

# Print a personalized message
print(f"Hello, {name}! You will turn 100 years old in the year {turn_year}")
