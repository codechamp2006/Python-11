# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes an amount and calculates the number of coins of each denomination
amt = int(input("Enter amount : "))

c500 = amt // 500
amt = amt % 500
c100 = amt // 100
amt = amt % 100
c50 = amt // 50
amt = amt % 50
c10 = amt // 10
amt = amt % 10
c1 = amt // 1

print("No of 500 coins : ", c500)
print("No of 100 coins : ", c100)
print("No of 50 coins : ", c50)
print("No of 10 coins : ", c10)
print("No of 1 coins : ", c1)
