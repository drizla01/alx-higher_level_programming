#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
cue = abs(number) % 10
sign = "" if number > 0 else "-"
if cue > 5:
    print("Last digit of {} is {}{} and is greater than 5 and not 0".format(number, sign, cue))
elif cue < 6 and cue != 0:
    print("Last digit of {} is {}{} and is less than 6 and not 0".format(number, sign, cue))
else:
    print("Last digit of {} is {} and is 0".format(number, cue))
