#!/usr/bin/python3
"""This module defines a BaseGeometry class with area and integer validation methods."""


class BaseGeometry:
    """A class that serves as a base for geometry-related classes."""

    def area(self):
        """Raises an Exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer, raising errors if not."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
