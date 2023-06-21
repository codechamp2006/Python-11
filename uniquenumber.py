# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes a number and checks if it is unique or not

num = int(input("Enter a number : "))
matched = False
for i in range(0, 10):
    count = 0
    copy = num

    while copy > 0:
        d = copy % 10
        if d == i:
            count = count + 1
        copy = copy // 10

    if count > 1:
        matched = True
        break


if matched:
    print("Not a unique number")
else:
    print("Unique number")
