# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes weight of parcel and calculates the cost of parcel
parcel = int(input("Enter weight of parcel : "))
cost = 0
if parcel <= 100:
    cost = 80
elif parcel > 100:
    cost += 80
    div = parcel // 50
    cost += 60 * div
    rem = parcel % 50
    if rem != 0:
        cost += 60

print("Cost of parcel is : ", cost)
