#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10;
if number < 0:
    digit = -digit
print("the number is {} and the last number is {}".format(number, digit), end=" ")
if digit > 5:
    print("is greater than 5")
elif digit == 0:
    print("0")
else:
    print("is less than 6 not 0")
