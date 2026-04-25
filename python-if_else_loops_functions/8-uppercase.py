#!/usr/bin/python3
def uppercase(str):
    for char in str:
        i = ord(char)
        if 97 <= i <= 122:
            i -= 32
        print("{}".format(chr(i)), end="")
    print("")
