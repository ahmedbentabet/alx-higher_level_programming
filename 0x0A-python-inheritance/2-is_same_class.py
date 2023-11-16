#!/usr/bin/python3
"""Exact same object module."""


def is_same_class(obj, a_class):
    """Checks if 'obj' is an instance of 'a_class'."""

    if type(obj) is a_class:
        return True
    else:
        return False
