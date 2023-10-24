#!/usr/bin/python3
"""This module defines a class Square that represents a square. """


class Square:
    """ A class named Square with private instance attributes size and position. """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the Square instance.

        Parameters:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Parameters:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) for i in value) \
                or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
