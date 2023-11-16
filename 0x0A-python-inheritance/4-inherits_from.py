#!/usr/bin/python3
""" 'Only sub class of' module. """


def inherits_from(obj, a_class):
    """Checks if 'obj' is an instance of subclass of 'a_class'."""

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
