#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
cue = number % 10
if cue > 5:
    print("Last digit of {} is {} and is greater than 5 and not 0".format(number, cue))
elif cue < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, cue))
else:
    print("Last digit of {} is {} and is 0".format(number, cue))
