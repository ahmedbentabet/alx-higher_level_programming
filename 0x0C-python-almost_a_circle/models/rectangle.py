#!/usr/bin/python3
"""This module defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        # Validate width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else: 
            self.__width = width

        # Validate height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else: 
            self.__height = height

        # Validate x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else: 
            self.__x = x

        # Validate y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else: 
            self.__y = y

        # Validate id
        if id is not None and type(id) is not int:
            raise TypeError("id must be an integer")
        else:
            super().__init__(id)


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        # Validate width
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else: 
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    # Validate height
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else: 
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        # Validate x
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else: 
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        # Validate y
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else: 
            self.__y = value
