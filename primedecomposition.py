# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes a number and prints the prime factors

num = int(input("Enter a number : "))
k = 2

while num >= k:
    if num % k == 0:
        print(k)
        num = num / k
    else:
        k = k + 1
