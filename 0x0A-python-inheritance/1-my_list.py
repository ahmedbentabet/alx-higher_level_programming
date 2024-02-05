#!/usr/bin/python3
"""Class 'MyList' inherits from class 'list'."""


class MyList(list):
    """A child class of the 'list' class."""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
