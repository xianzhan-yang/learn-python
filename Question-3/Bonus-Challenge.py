num = int(input("Enter a number: "))

if num > 0:
    sign = "positive"
elif num < 0:
    sign = "negative"
else:
    sign = "zero"

if num % 2 == 0:
    even_odd = "even"
else:
    even_odd = "odd"

print(f"The number {num} is {sign} and {even_odd}")
