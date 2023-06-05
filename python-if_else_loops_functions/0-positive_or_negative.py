#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for i in range(number):
    if i >= 0:
        print ("is positive")
    if i == 0:
        print ("is zero")
    if i <= 0:
        print ("is negative")
