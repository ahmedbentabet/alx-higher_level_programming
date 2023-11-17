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

        BaseGeometry.integer_validator("width", width)
        self.__width = width
        BaseGeometry.integer_validator("height", height)
        self.__height = height
