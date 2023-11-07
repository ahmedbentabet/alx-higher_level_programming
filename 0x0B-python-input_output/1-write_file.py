#!/usr/bin/python3
""" write string to file """


def write_file(filename="", text=""):
    """ writes a string to a text file and returns the num of chars written """

    num_of_char = 0
    with open(filename, "w", encoding="utf-8") as my_file:
        my_file.write(text)
    for i in text:
        num_of_char += 1

    return num_of_char
