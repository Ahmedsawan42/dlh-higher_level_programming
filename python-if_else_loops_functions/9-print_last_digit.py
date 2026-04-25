#!/usr/bin/python3

def print_last_digit(number):
    if isinstance(number, (int, float)):
        text = str(number)
        print(text[-1], end="")
        return (text[-1])
