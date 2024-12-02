# Ask the user for a list of numbers (separated by commas)
numbers_input = input("Enter numbers separated by commas: ")

# Convert the string input into a list of integers
numbers_list = [int(num) for num in numbers_input.split(",")]

# Calculate sum, average, even and odd counts
sum_of_numbers = sum(numbers_list)
average = sum_of_numbers / len(numbers_list) if numbers_list else 0
even_count = sum(1 for num in numbers_list if num % 2 == 0)
odd_count = len(numbers_list) - even_count  # The rest are odd

# Find the largest and smallest numbers
largest_number = max(numbers_list)
smallest_number = min(numbers_list)

# Print the results
print(f"Sum of numbers: {sum_of_numbers}")
print(f"Average of numbers: {average:.2f}")
print(f"Even numbers count: {even_count}")
print(f"Odd numbers count: {odd_count}")

# Print the largest and smallest numbers
print(f"Largest number: {largest_number}")
print(f"Smallest number: {smallest_number}")
