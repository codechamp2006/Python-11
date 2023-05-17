# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes two numbers and calculates the HCF

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
min = 0
hcf = 0

abs_a = abs(a)
abs_b = abs(b)

if abs_a < abs_b:
    min = abs_a
else:
    min = abs_b

for i in range(1, min + 1):
    if abs_a % i == 0 and abs_b % i == 0:
        hcf = i

print("HCF of ", a, " and ", b, " is ", hcf)
