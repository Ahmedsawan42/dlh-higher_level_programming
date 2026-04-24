#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = -5224
str = str(number)
last = str[-1]
if int(last) > 5 and number > 0:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif int(last) == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif number > 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is -{last} and is less than 6 and not 0")
