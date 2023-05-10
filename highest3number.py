# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes three numbers and determines the highest of them
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

max = num1
if num2 > max:
    max = num2
if num3 > max:
    max = num3

print("Highest of three numbers : ", max)
