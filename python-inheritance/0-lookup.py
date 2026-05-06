#!/usr/bin/python3
"""Module that provides a function to look up object attributes and methods."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: Any Python object.

    Returns:
        list: A list of strings naming the object's attributes and methods.
    """
    return dir(obj)
