# Ask the user to enter a word
word = input("Enter a word: ")

# Reverse the word
reversed_word = word[::-1]

# Convert the word to uppercase and lowercase
uppercase_word = word.upper()
lowercase_word = word.lower()

# Check if the word is a palindrome
if word == reversed_word:
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")

# Print the results
print(f"Reversed word: {reversed_word}")
print(f"Uppercase word: {uppercase_word}")
print(f"Lowercase word: {lowercase_word}")