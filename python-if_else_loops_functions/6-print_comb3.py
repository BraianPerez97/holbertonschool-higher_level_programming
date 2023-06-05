#!/usr/bin/python3
for num1 in range(0, 9):
    for num2 in range(num1 + 1, 10):
        print("{:02d}".format(num1) + "{:02d}".format(num2), end=", ")
print("89")
