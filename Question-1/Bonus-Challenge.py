# Question
# Enhance the program to ask the user for their age and calculate the year they'll turn 100.
#
# Example Input/Output:
# What is your name? Bob
# How old are you? 25
# Hello, Bob! You will turn 100 years old in the year 2099.

name = input("What is your name? ")
age = int(input("How old are you? "))

current_year = 2024
turn_year = current_year + (100 - age)

print(f"Hello, {name}! You will turn 100 years old in the year {turn_year}")
