#!/usr/bin/python3
"""Module for the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value

    def __str__(self):
        """Return a string representation of the Square."""
        return (
            f"[{self.__class__.__name__}] ({self.id}) "
            f"{self.x}/{self.y} - {self.size}"
        )

    def update(self, *args, **kwargs):
        """Update Square."""
        attributes = ['id', 'size', 'x', 'y']

        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for attr_name, attr_value in kwargs.items():
                setattr(self, attr_name, attr_value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        Square_dict = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return Square_dict