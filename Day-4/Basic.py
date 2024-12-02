# Ask the user for a list of numbers (separated by spaces)
numbers = input("Enter numbers separated by spaces: ")

# Convert the string input into a list of integers
numbers_list = [int(num) for num in numbers.split()]

# Calculate sum, largest, and smallest numbers
sum_of_numbers = sum(numbers_list)
largest_number = max(numbers_list)
smallest_number = min(numbers_list)

# Print the results
print(f"Sum of numbers: {sum_of_numbers}")
print(f"Largest number: {largest_number}")
print(f"Smallest number: {smallest_number}")
