#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for i in range(number):
    if number >= 0:
        print("{:d}is positive")
    if number == 0:
        print ("{:d}is zero")
    if number <= 0:
        print ("{:d}is negative")
