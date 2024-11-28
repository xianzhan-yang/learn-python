# Question:
# Write a Python program that asks the user to 
# input two numbers and then outputs the sum, 
# difference, product, and quotient of those numbers.
#
# Example Input/Output:
# Enter the first number: 5
# Enter the second number: 3
# Sum: 8
# Difference: 2
# Product: 15
# Quotient: 1.6666666666666667

num1 = float(input("Enter the first number: " ))
num2 = float(input("Enter the second number: " ))

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2

print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Project: {product_result}")
print(f"Quotient: {quotient_result}")
