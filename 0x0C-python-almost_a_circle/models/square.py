#!/usr/bin/python3
"""Module for the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size

    def __str__(self):
        """Return a string representation of the Square."""
        return (
            f"[{self.__class__.__name__}] ({self.id}) "
            f"{self.x}/{self.y} - {self.size}"
        )
