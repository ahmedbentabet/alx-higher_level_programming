#!/usr/bin/python3
"""Define The addition function."""


def add_integer(a, b=98):
    """Add two integers"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

# print(add_integer(float('inf')))
print(type(float('inf')))
