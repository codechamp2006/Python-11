# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes a number and checks if it is an armstrong number

num = int(input("Enter a number : "))
copy = num
sum = 0
count = 0

while copy > 0:
    count = count + 1
    copy = copy // 10

copy = num
while copy > 0:
    d = copy % 10
    sum = sum + d ** count
    copy = copy // 10

if sum == num:
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")
