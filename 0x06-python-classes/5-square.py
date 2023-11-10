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

    @property
    def size(self):
        """Get the size of the square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Set a new size to the square."""

        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square."""

        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #."""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
