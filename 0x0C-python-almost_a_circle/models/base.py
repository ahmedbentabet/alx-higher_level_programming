#!/usr/bin/python3
"""This module defines the Base class."""


class Base:
    """the Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
