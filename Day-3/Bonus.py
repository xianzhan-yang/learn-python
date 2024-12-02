# Ask the user for a number
number = int(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    sign = "positive"
elif number < 0:
    sign = "negative"
else:
    sign = "zero"

# Check if the number is even or odd
if number % 2 == 0:
    even_odd = "even"
else:
    even_odd = "odd"

# Print the results
print(f"The number {number} is {sign} and {even_odd}.")
