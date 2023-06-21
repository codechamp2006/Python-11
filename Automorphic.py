# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes a number and checks if it is an automorphic number

num = int(input("Enter a number : "))
copy = num ** 2
count = 0
sum = 0

while copy > 0:
    d = copy % 10
    rev = d * (10 ** count)
    sum = sum + rev
    if(sum == num):
        break
    else:
        continue
    count = count + 1
    copy = copy // 10

if sum == num:
    print(num, "is an automorphic number")
else:
    print(num, "is not an automorphic number")
