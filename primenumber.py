# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes a number and checks if it is prime or not

num = int(input("Enter a number : "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")

