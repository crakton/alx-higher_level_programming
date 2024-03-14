#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
val = abs(number) % 10
if number < 0:
    val = -val
print(f"Last digit of {number} is {val} and is ", end="")
if val == 0:
    print("0")
elif val > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
