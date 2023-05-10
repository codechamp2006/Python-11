# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes two sets of time and adds them

h1 = int(input("Enter hour of first time : "))
m1 = int(input("Enter minutes of first time : "))
s1 = int(input("Enter seconds of first time : "))
h2 = int(input("Enter hour of second time : "))
m2 = int(input("Enter minutes of second time : "))
s2 = int(input("Enter seconds of second time : "))

h = h1 + h2
m = m1 + m2
s = s1 + s2

m = m + s // 60
s = s % 60
h = h + m // 60
m = m % 60
print(h, ":", m, ":", s)
