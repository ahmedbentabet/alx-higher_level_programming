#!/usr/bin/python3
"""Define a class Square that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """"A class that inherits from Rectangle."""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"


s = Square(13)

print(s)
print(s.area())
