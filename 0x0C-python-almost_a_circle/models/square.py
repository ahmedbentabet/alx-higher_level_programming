#!/usr/bin/python3
"""efergfre"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """fdfsdf"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, width, height)
        self.size = width

    def __str__(self):
        """Return a string representation of the Square."""
        return (
            f"[{self.__class__.__name__}] ({self.id}) "
            f"{self.x}/{self.y} - {self.size}"
        )
