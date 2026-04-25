#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = str(number)
last = str[-1]
last_num = int(last)
if int(last) > 5 and number > 0:
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif int(last) == 0:
    print(f"Last digit of {number} is {last_num} and is 0")
elif number > 0:
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")
else:
    last_num = last_num * -1
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")
