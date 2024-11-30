numbers = input("Enter numbers separated by spaces: ")

numbers_list = [int(num) for num in numbers.split()]

sum_of_numbers = sum(numbers_list)
largest_number = max(numbers_list)
smallest_number = min(numbers_list)
average = sum_of_numbers / len(numbers_list)

print(f"Sum of numbers: {sum_of_numbers}")
print(f"Largest number: {largest_number}")
print(f"Smallest number: {smallest_number}")
print(f"Average of numbers: {average}")

