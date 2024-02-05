#!/usr/bin/python3
"""Define a class Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """"A class that inherits from BaseGeometry."""

    def __init__(self, width, height):

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
