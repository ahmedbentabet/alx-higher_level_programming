#!/usr/bin/python3
"""Exact same object module."""


def is_same_class(obj, a_class):
    """Check instantiation."""

    if isinstance(obj, a_class):
        return True
    else:
        return False
