#!/usr/bin/python3
"""Exact same object module."""


def is_same_class(obj, a_class):
    """Check instantiation."""

    if type(obj) is a_class:
        return True
    else:
        return False
