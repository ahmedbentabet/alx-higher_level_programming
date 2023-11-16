#!/usr/bin/python3
"""Same class or inherit from module."""


def is_kind_of_class(obj, a_class):
    """Checks if 'obj' is an instance of 'a_class' or a subclass of it."""

    if isinstance(obj, a_class):
        return True
    else:
        return False
