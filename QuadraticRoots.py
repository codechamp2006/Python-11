# Author codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes a, b and c as input and calculates the roots of the quadratic equation

a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))
d = (b ** 2) - (4 * a * c)
if d < 0:
    print("Roots are imaginary")
else:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Root 1 = ", root1)
    print("Root 2 = ", root2)

if d == 0:
    print("Roots are real and equal")
elif d > 0:
    print("Roots are real and unequal")

