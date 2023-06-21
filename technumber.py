# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes a number and checks if it is a technumber

num = int(input("Enter a number : "))
copy = num
count = 0

while copy > 0:
    count = count + 1
    copy = copy // 10

copy = num

last = copy % (10 ** (count//2))
first = copy // (10 ** (count//2))
sum = last + first

copy = sum ** 2
if copy == num:
    print("Technumber")
else:
    print("Not Technumber")
