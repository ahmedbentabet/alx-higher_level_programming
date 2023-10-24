#!/usr/bin/python3

"""This module defines a class Square that represents a square."""


class Square:
    """A Square with a private instance attribute size."""

    def __init__(self, size):
        """
        Initializes the Square instance.

        Parameters:
            size (int): The size of the square.
        """
        self.__size = size
