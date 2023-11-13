#!/usr/bin/python3
"""Define the Square class"""


class Square:
    """A Square with a private instance attribute."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square."""

        self.__size = size
        if not isinstance(position, tuple) or len(position) != 2 \
                    or not all(isinstance(i, int) for i in position) \
                    or position[0] < 0 or position[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """Get the size of the square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Set a new size to the square."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) for i in value) \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""

        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #."""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
