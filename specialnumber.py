# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes a number and checks if it is special number or not

num = int(input("Enter a number : "))
sum = 0
copy = num

while copy > 0:
    d = copy % 10
    prod = 1
    for i in range(1, d + 1):
        prod = prod * i
    sum = sum + prod
    copy = copy // 10

if sum == num:
    print("Special number")
else:
    print("Not a special number")
