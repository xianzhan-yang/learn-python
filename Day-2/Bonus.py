# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

# Check for division by zero
if num2 != 0:
    quotient_result = num1 / num2
else:
    quotient_result = "Error: Cannot divide by zero"

# Display the results
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")
