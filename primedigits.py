# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes a number and prints the prime digits

num = int(input("Enter a number : "))

while(num > 0):
    d = num % 10
    if d == 2 or d == 3 or d == 5 or d == 7:
        print(d)
    num = num // 10
