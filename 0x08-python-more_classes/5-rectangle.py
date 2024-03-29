#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width * self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        if self.width * self.height == 0:
            return ''
        else:
            return "\n".join("#" * self.width for _ in range(self.height))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self. height)

    def __del__(self):
        print("Bye rectangle...")
