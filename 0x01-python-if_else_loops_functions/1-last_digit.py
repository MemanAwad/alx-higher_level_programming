#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    negative = number * -1
    last = number % 10
    print("Last digit of {} is {} and is less than ")
print(last)
