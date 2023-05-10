# Author: codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes base and power and calculates the power of the base
x = int(input("Enter base : "))
y = int(input("Enter power : "))

if y < 0:
    x = y * -1
pow = 1
for i in range(y):
    pow = pow * x

if y < 0:
    pow = 1 / pow

print(pow)