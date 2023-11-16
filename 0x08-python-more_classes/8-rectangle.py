#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """A class representing a rectangle."""

    number_of_instances = 0

    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if (Rectangle.area(rect_1) >= Rectangle.area(rect_2)):
            return rect_1
        else:
            return rect_2

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            return ('')
        else:
            return ("\n".join(str(self.print_symbol) * self.width
                    for _ in range(self.height)))

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
