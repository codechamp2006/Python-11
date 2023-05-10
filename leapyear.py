# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes a year and determines if it is a leap year or not
year = int(input("Enter a year: "))
if year % 4 == 0:
    print("Leap year")
elif year % 400 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not a leap year")
