#!/usr/bin/python3
"""Define BaseGeometry & Rectangle classes."""


class BaseGeometry:
    """A class representing a BaseGeometry."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """"A class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        super().__init__()

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
