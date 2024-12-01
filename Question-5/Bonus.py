word = input("Enter a word: ")

word_reversed = word[::-1]

if word == word_reversed:
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")

word_upper = word.upper()
word_lower = word.lower()

print(f"Reversed word: {word_reversed}")
print(f"Uppercase word: {word_upper}")
print(f"Lowercase word: {word_lower}")
