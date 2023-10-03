#!/usr/bin/python3

def uppercase(str):
    uppercase_str = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            uppercase_str += chr(ord(c) - 32)
        else:
            uppercase_str += c
    print("{}".format(uppercase_str))
