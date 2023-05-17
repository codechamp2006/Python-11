# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# to find highest and lowest number and calculate their difference

n = int(input("Enter number of elements : "))
max,min,num = 0,0,0
for i in range(n):
    num = int(input("Enter number:"))
    if i == 0:
        max = num
        min = num
    if num > max:
        max = num
    if num < min:
        min = num

print("Highest number : ", max)
print("Lowest number : ", min)
print("Difference : ", max - min)