# Author : codechamp27
# Code Licensed under the Apache License, Version 2.0
# takes time in seconds and converts it to hours, minutes and seconds
time = int(input("Enter a time in seconds: "))
hour = time // 3600
time = time % 3600
minute = time // 60
time = time % 60
second = time
print(hour, ":", minute, ":", second)