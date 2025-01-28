num1 = int(input("Enter the first number (num1): "))
num2 = int(input("Enter the second number (num2): "))

print("Before swapping: num1 = {num1}, num2 = {num2}")

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping: num1 = {num1}, num2 = {num2}")