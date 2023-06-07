# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes a number and checks if it is a perfect number

num = int(input("Enter a number : "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")
