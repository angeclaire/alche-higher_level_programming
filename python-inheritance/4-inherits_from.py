#!/usr/bin/python3
"""Module that defines the inherits_from function."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class only.

    Args:
        obj: Any Python object.
        a_class: The class to check against.

    Returns:
        bool: True if obj's class inherits from a_class, else False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
