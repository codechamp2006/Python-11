# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes a number and checks if it is a triangular number

num = int(input("Enter a number : "))
triangular = False
sum = 0
for i in range(1, num):
    sum += i
    if sum == num:
        triangular = True
        break
    else:
        continue

if triangular == True:
    print(num, "is a triangular number")
else:
    print(num, "is not a triangular number")