#!/usr/bin/python3
for num in range(0, 100):
    if num <= 9:
        print("0{},".format(num), end=" ")
    elif num >= 10 and num < 99:
        print("{},".format(num), end=" ")
    elif num == 99:
        print("{}".format(num))
