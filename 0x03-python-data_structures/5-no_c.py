#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for chr in my_string:
        if chr != 'c' and chr != 'C':
            new_string = new_string + chr
    return new_string
