#!/usr/bin/python3
"""Define the Squire class"""


class Square:
    """A Square with a private instance attribute."""

    def __init__(self, size=0):
        """
        Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square."""

        return self.__size * self.__size
