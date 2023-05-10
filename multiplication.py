# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0

x = int(input("Enter value of x : "))
y = int(input("Enter value of y : "))

sum = 0
if (x > 0 and y < 0) or (x < 0 and y > 0):
    x = x * -1

for i in range(abs(y)):
    sum += x

print(sum)
