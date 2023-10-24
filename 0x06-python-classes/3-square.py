#!/usr/bin/python3

"""A class Square that represents a square."""


class Square:
    """ Square with a private instance attribute size. """

    def __init__(self, size=0):
        """
        Initializes the Square instance.

        Parameters:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
