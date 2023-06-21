# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes a number and checks if it is a kaprekar number

num = int(input("Enter a number : "))
copy = num
count = 0

while copy > 0:
    count = count + 1
    copy = copy // 10

copy = num ** 2

last = copy % (10 ** count)
first = copy // (10 ** count)
sum = last + first

if sum == num:
    print(num, "is a kaprekar number")
else:
    print(num, "is not a kaprekar number")
