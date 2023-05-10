# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes three sides of a triangle and determines the type of triangle
s1 = int(input("Enter side 1 : "))
s2 = int(input("Enter side 2 : "))
s3 = int(input("Enter side 3 : "))

if s1 == s2 and s2 == s3 and s1 == s3:
    print("Equilateral Triangle")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
