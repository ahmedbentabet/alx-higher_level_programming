#!/usr/bin/python3
""" Append string to file. """


def append_write(filename="", text=""):
    """ Append a string to a text file and returns the num of chars written. """

    num_of_char = 0
    with open(filename, "a", encoding="utf-8") as my_file:
        my_file.write(text)
    for i in text:
        num_of_char += 1

    return num_of_char
